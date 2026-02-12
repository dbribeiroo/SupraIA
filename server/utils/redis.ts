import Redis from "ioredis"

let redis: Redis | null = null

export function getRedis() {
  if (!redis) {
    const redisUrl = process.env.REDIS_URL || "redis://redis:6379"
    
    redis = new Redis(redisUrl, {
      maxRetriesPerRequest: 3,
      retryStrategy(times) {
        const delay = Math.min(times * 50, 2000)
        return delay
      }
    })
  }
  
  return redis
}

export default getRedis()
