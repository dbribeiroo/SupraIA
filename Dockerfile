# Development stage
FROM oven/bun:1.2 AS dev
WORKDIR /app

COPY package.json ./
COPY bun.lock* bun.lockb* ./

RUN bun install

EXPOSE 3000

CMD ["bun", "run", "dev", "--host", "0.0.0.0"]

# Build stage
FROM oven/bun:1.2 AS build
WORKDIR /app

COPY package.json ./
COPY bun.lock* bun.lockb* ./

RUN bun install

COPY . .

RUN bun run build

# Production stage
FROM oven/bun:1.2 AS production
WORKDIR /app

COPY --from=build /app/.output ./.output

ENV HOST=0.0.0.0
ENV PORT=3000
ENV NODE_ENV=production

EXPOSE 3000

CMD ["bun", "run", ".output/server/index.mjs"]
