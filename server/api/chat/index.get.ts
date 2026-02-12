import { getRedis } from "#imports"

export default defineEventHandler(async (event) => {
  try {
    const redis = getRedis()
    const keys = await redis.keys("chat:*")
    
    if (keys.length === 0) {
      return {
        success: true,
        data: []
      }
    }
    
    const chats = await Promise.all(
      keys.map(async (key) => {
        const messages = await redis.lrange(key, 0, 0)
        const firstMessage = messages[0] ? JSON.parse(messages[0]) : null
        const ttl = await redis.ttl(key)
        
        return {
          id: key.replace("chat:", ""),
          titulo: firstMessage?.content?.substring(0, 50) + "..." || "Nova conversa",
          ttl,
          firstMessage
        }
      })
    )

    return {
      success: true,
      data: chats
    }
  } catch (error) {
    console.error("Erro ao listar chats:", error)
    throw createError({
      statusCode: 500,
      message: "Erro ao listar chats ativos"
    })
  }
})
