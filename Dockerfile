# Development stage
FROM oven/bun:1.2 AS dev
WORKDIR /app

# Install OpenSSL for Prisma
RUN apt-get update -y && apt-get install -y openssl

# Copy package files
COPY package.json ./
COPY bun.lock* bun.lockb* ./

# Copy prisma schema BEFORE installing
COPY prisma ./prisma

# Install dependencies
RUN bun install

# Generate Prisma Client
RUN bunx prisma generate

EXPOSE 3000

CMD ["bun", "run", "dev", "--host", "0.0.0.0"]

# Build stage
FROM oven/bun:1.2 AS build
WORKDIR /app

# Install OpenSSL for Prisma
RUN apt-get update -y && apt-get install -y openssl

COPY package.json ./
COPY bun.lock* bun.lockb* ./

# Copy prisma schema
COPY prisma ./prisma

RUN bun install

# Generate Prisma Client
RUN bunx prisma generate

COPY . .

RUN bun run build

# Production stage
FROM oven/bun:1.2 AS production
WORKDIR /app

# Install OpenSSL for Prisma
RUN apt-get update -y && apt-get install -y openssl

COPY --from=build /app/.output ./.output
COPY --from=build /app/node_modules/.prisma ./node_modules/.prisma
COPY --from=build /app/node_modules/@prisma ./node_modules/@prisma

ENV HOST=0.0.0.0
ENV PORT=3000
ENV NODE_ENV=production

EXPOSE 3000

CMD ["bun", "run", ".output/server/index.mjs"]
