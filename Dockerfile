FROM oven/bun:1.2 AS dev
WORKDIR /app

RUN apt-get update -y && apt-get install -y openssl

COPY package.json ./
COPY bun.lock* bun.lockb* ./

COPY prisma ./prisma

RUN bun install

RUN bunx prisma generate

EXPOSE 3000

CMD ["bun", "run", "dev", "--host", "0.0.0.0"]

FROM oven/bun:1.2 AS build
WORKDIR /app

RUN apt-get update -y && apt-get install -y openssl

COPY package.json ./
COPY bun.lock* bun.lockb* ./

COPY prisma ./prisma

RUN bun install

RUN bunx prisma generate

COPY . .

RUN bun run build

FROM oven/bun:1.2 AS production
WORKDIR /app

RUN apt-get update -y && apt-get install -y openssl

COPY --from=build /app/.output ./.output
COPY --from=build /app/node_modules/.prisma ./node_modules/.prisma
COPY --from=build /app/node_modules/@prisma ./node_modules/@prisma

ENV HOST=0.0.0.0
ENV PORT=3000
ENV NODE_ENV=production

EXPOSE 3000

CMD ["bun", "run", ".output/server/index.mjs"]
