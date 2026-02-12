FROM python:3.12-slim AS dev
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml ./

RUN uv sync --no-install-project

COPY . .

EXPOSE 7777

CMD ["uv", "run", "fastapi", "dev", "agent.py", "--host", "0.0.0.0", "--port", "7777"]

FROM python:3.12-slim AS production
WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY pyproject.toml ./

RUN uv sync --no-dev --no-install-project

COPY . .

ENV HOST=0.0.0.0
ENV PORT=7777

EXPOSE 7777

CMD ["uv", "run", "fastapi", "run", "agent.py", "--host", "0.0.0.0", "--port", "7777"]
