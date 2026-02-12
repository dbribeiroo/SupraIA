import { getRedis, getPrisma } from "#imports"

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
    const prisma = getPrisma()
    
    await redis.del(`chat:${id}`)
    
    await prisma.mensagem.deleteMany({
      where: { conversaId: id }
    })
    
    await prisma.conversa.delete({
      where: { id }
    })

    return {
      success: true,
      message: "Conversa deletada com sucesso"
    }
  } catch (error: any) {
    console.error("Erro ao deletar chat:", error)
    
    throw createError({
      statusCode: 500,
      message: "Erro ao deletar conversa"
    })
  }
})
