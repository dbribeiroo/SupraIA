import OpenAI from 'openai';

export default defineEventHandler(async (event) => {
  const config = useRuntimeConfig();
  
  if (!config.openaiKey) {
    throw createError({
      statusCode: 500,
      statusMessage: 'Erro de Configuração: API Key não encontrada.',
    });
  }

  const openai = new OpenAI({
    apiKey: config.openaiKey,
  });

  const body = await readBody(event);
  const messages = body.messages || [];

  try {
    const completion = await openai.chat.completions.create({
      model: "gpt-4o",
      messages: [
    
        { 
          role: "system", 
          content: `
            Você é o Supra, o mascote amigável da Supranet (um provedor de internet fibra óptica da região do Vale do Aço).
            
            Suas regras de personalidade:
            - Você é entusiasta, usa emojis 🚀💻 e fala de forma jovem, mas profissional.
            - Seu objetivo é ajudar clientes com dúvidas sobre internet, wi-fi e velocidade.
            - Se perguntarem quem é você, diga que é o Supra, mascote da Supranet.
            - Responda sempre em Português do Brasil.
            - Seja conciso e direto.
            - Sempre lembre as pessoas de que a Supranet é o melhor provedor de internet do Leste de Minas!
          ` 
        },
        ...messages
      ],
    });

    return {
      message: completion.choices[0].message
    };

  } catch (error) {
    console.error('Erro na OpenAI:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'O Supra está dormindo um pouco (Erro no servidor).',
    });
  }
});