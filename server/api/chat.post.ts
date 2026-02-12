import { getRedis, getPrisma } from "#imports"

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  const agentApiUrl = config.agentApiUrl || 'http://localhost:7777';

  const body = await readBody(event);
  const messages = body.messages || [];
  const conversaId = body.conversaId || `conversa:${Date.now()}`;

  const lastUserMessage = [...messages].reverse().find((m: any) => m.role === 'user');

  if (!lastUserMessage) {
    throw createError({
      statusCode: 400,
      statusMessage: 'Nenhuma mensagem de usuário encontrada.',
    });
  }

  try {
    const redis = getRedis()
    const prisma = getPrisma()
    
    // Save user message to Redis
    const userMessage = {
      role: 'user',
      content: lastUserMessage.content,
      timestamp: Date.now()
    }
    
    await redis.rpush(`chat:${conversaId}`, JSON.stringify(userMessage))
    await redis.expire(`chat:${conversaId}`, 86400)

    // Call agent
    const formData = new FormData();
    formData.append('message', lastUserMessage.content);
    formData.append('stream', 'false');

    const response = await fetch(`${agentApiUrl}/agents/supra/runs`, {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const err = await response.text();
      console.error('AgentOS error:', response.status, err);
      throw new Error(err);
    }

    const data = await response.json();

    const assistantMessage = {
      role: 'assistant',
      content: data.content,
      timestamp: Date.now()
    }
    
    await redis.rpush(`chat:${conversaId}`, JSON.stringify(assistantMessage))

    let conversa = await prisma.conversa.findFirst({
      where: { id: conversaId }
    })
    
    if (!conversa) {
      conversa = await prisma.conversa.create({
        data: {
          id: conversaId,
          titulo: lastUserMessage.content.substring(0, 50) + '...'
        }
      })
    }

    await prisma.mensagem.createMany({
      data: [
        {
          conversaId: conversa.id,
          role: 'user',
          content: lastUserMessage.content
        },
        {
          conversaId: conversa.id,
          role: 'assistant',
          content: data.content
        }
      ]
    })

    return {
      conversaId,
      message: {
        role: 'assistant',
        content: data.content,
      },
    };
  } catch (error: any) {
    console.error('Erro no AgentOS:', error?.message || error);
    throw createError({
      statusCode: 500,
      statusMessage: 'O Supra está dormindo um pouco (Erro no servidor).',
    });
  }
});
