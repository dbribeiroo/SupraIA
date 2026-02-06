export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  const agentApiUrl = config.agentApiUrl || 'http://localhost:7777';

  const body = await readBody(event);
  const messages = body.messages || [];

  const lastUserMessage = [...messages].reverse().find((m: any) => m.role === 'user');

  if (!lastUserMessage) {
    throw createError({
      statusCode: 400,
      statusMessage: 'Nenhuma mensagem de usuário encontrada.',
    });
  }

  try {
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

    return {
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
