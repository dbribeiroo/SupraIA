import { getRedis } from "#imports"

export default defineEventHandler(async (event) => {
  try {
    const id = getRouterParam(event, "id")
    
    if (!id) {
      throw createError({
        statusCode: 400,
        message: "ID da conversa é obrigatório"
      })
    }
    
    const redis = getRedis()
    const messages = await redis.lrange(`chat:${id}`, 0, -1)
    
    if (messages.length === 0) {
      throw createError({
        statusCode: 404,
        message: "Conversa não encontrada"
      })
    }
    
    const parsedMessages = messages.map(msg => JSON.parse(msg))

    return {
      success: true,
      data: {
        conversaId: id,
        mensagens: parsedMessages
      }
    }
  } catch (error: any) {
    console.error("Erro ao buscar chat:", error)
    
    if (error.statusCode) {
      throw error
    }
    
    throw createError({
      statusCode: 500,
      message: "Erro ao buscar histórico do chat"
    })
  }
})
