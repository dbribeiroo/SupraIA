<div align="center">

# 🚀 SupraIA

**Agente Inteligente com Busca Web e Persistência de Dados**

*Chat AI moderno com histórico de conversas, cache Redis e banco PostgreSQL*

[![Nuxt](https://img.shields.io/badge/Nuxt-4.x-00DC82.svg)](https://nuxt.com/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7-DC382D.svg)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Sobre](#-sobre) • [Funcionalidades](#-funcionalidades) • [Tecnologias](#-tecnologias) • [Como Rodar](#-como-rodar) • [Arquitetura](#-arquitetura) • [Interfaces](#-interfaces-administrativas)

</div>

---

## 📖 Sobre

**SupraIA** é uma aplicação full-stack de chat com inteligência artificial que combina:

- 🤖 **IA Generativa** (OpenAI GPT-4) com busca web em tempo real
- 💾 **Persistência de dados** com PostgreSQL + Prisma ORM
- ⚡ **Cache Redis** para performance otimizada
- 🎨 **Interface moderna** com Nuxt 4 + Vue 3 + Nuxt UI
- 🐳 **Containerização completa** com Docker Compose
- 📊 **Ferramentas administrativas** (Prisma Studio, PgAdmin, Redis Commander)

O projeto foi desenvolvido como portfólio profissional, demonstrando habilidades em:
- Arquitetura de microsserviços
- Integração frontend/backend
- Gerenciamento de estado e cache
- DevOps e containerização
- Boas práticas de desenvolvimento

---

## ✨ Funcionalidades

### 🎯 Implementadas

- [x] **Chat com IA** - Interface conversacional com GPT-4
- [x] **Busca Web em Tempo Real** - DuckDuckGo Search integrado ao agente
- [x] **Histórico de Conversas** - Sidebar com lista de conversas anteriores
- [x] **Persistência Dupla** - Redis (cache 24h) + PostgreSQL (permanente)
- [x] **CRUD Completo** - Criar, listar, carregar e deletar conversas
- [x] **Cache Inteligente** - Redis para acesso rápido, PostgreSQL para backup
- [x] **Interface Responsiva** - Design moderno com Nuxt UI + Tailwind
- [x] **Containerização** - Docker Compose com 6 serviços integrados
- [x] **Ferramentas Admin** - Prisma Studio, PgAdmin, Redis Commander
- [x] **API REST** - Endpoints documentados e organizados
- [x] **Markdown Rendering** - Formatação de respostas da IA

### 🔄 Próximas Melhorias

- [ ] **Autenticação** - Sistema de login com sessões
- [ ] **Multi-usuário** - Suporte a múltiplos usuários simultâneos
- [ ] **Upload de Arquivos** - Análise de documentos pelo agente
- [ ] **Streaming de Respostas** - Respostas em tempo real (SSE)
- [ ] **Temas** - Dark mode / Light mode
- [ ] **Exportar Conversas** - Download em PDF/JSON
- [ ] **Busca no Histórico** - Filtrar conversas antigas

---

## 🛠️ Stack Tecnológica

### Frontend

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Nuxt** | 4.x | Framework Vue.js full-stack |
| **Vue** | 3.x | Framework JavaScript reativo |
| **Nuxt UI** | Latest | Biblioteca de componentes |
| **Tailwind CSS** | 3.x | Framework CSS utility-first |
| **TypeScript** | 5.x | Tipagem estática |

### Backend

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **Python** | 3.11+ | Linguagem do agente IA |
| **Agno (AgentOS)** | Latest | Framework para agentes IA |
| **OpenAI API** | GPT-4 | Modelo de linguagem |
| **DuckDuckGo Search** | 8.x | Busca web integrada |
| **Nuxt Server** | 4.x | API Routes (backend Nuxt) |
| **Bun** | Latest | Runtime JavaScript moderno |

### Banco de Dados & Cache

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| **PostgreSQL** | 16 | Banco relacional principal |
| **Prisma** | 6.x | ORM moderno para TypeScript |
| **Redis** | 7 | Cache em memória (TTL 24h) |

### DevOps & Ferramentas

| Tecnologia | Descrição |
|------------|-----------|
| **Docker** | Containerização |
| **Docker Compose** | Orquestração de 6 serviços |
| **Prisma Studio** | Interface visual PostgreSQL |
| **PgAdmin** | Admin avançado PostgreSQL |
| **Redis Commander** | Interface visual Redis |

---

## 🚀 Como Rodar

### Pré-requisitos

- **Docker** e **Docker Compose** instalados
- **Chave de API da OpenAI** ([obter aqui](https://platform.openai.com/api-keys))

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/dbribeiroo/SupraIA.git
cd SupraIA
```

### 2️⃣ Configure as variáveis de ambiente

```bash
# Criar .env na raiz
cat > .env << 'EOL'
DATABASE_URL="postgresql://suprauser:suprapass@db:5432/supradb"
REDIS_URL="redis://redis:6379"
OPENAI_API_KEY=sua-chave-openai-aqui
EOL

# Criar .env no supra-agent
cat > supra-agent/.env << 'EOL'
OPENAI_API_KEY=sua-chave-openai-aqui
EOL
```

### 3️⃣ Suba os containers

```bash
docker compose up -d --build
```

### 4️⃣ Crie as tabelas no banco

```bash
docker compose exec app bun prisma generate
docker compose exec app bun prisma db push
```

### 5️⃣ Acesse a aplicação

```bash
open http://localhost:3001
```

---

## 🌐 Interfaces Disponíveis

| Interface | URL | Credenciais | Descrição |
|-----------|-----|-------------|-----------|
| **App Principal** | http://localhost:3001 | - | Chat com IA |
| **Prisma Studio** | http://localhost:5555 | - | Ver/Editar PostgreSQL |
| **PgAdmin** | http://localhost:5050 | admin@supraia.com / admin123 | Admin PostgreSQL |
| **Redis Commander** | http://localhost:8081 | - | Ver cache Redis |
| **Python Agent API** | http://localhost:7777 | - | API do agente IA |

### 🔧 Comandos Úteis

```bash
# Abrir Prisma Studio
docker compose exec -d app bun prisma studio --hostname 0.0.0.0 --port 5555

# Ver logs em tempo real
docker compose logs -f app

# Acessar Redis CLI
docker compose exec redis redis-cli

# Acessar PostgreSQL CLI
docker compose exec db psql -U suprauser -d supradb

# Reiniciar tudo
docker compose restart

# Parar tudo
docker compose down

# Limpar volumes (CUIDADO: apaga dados)
docker compose down -v
```

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND (Nuxt 4)                       │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │  index.vue   │───▶│ useSupraIA() │───▶│  API Routes  │       │
│  │ (Interface)  │    │ (Composable) │    │ (/api/chat)  │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  HistoricoSidebar.vue - Lista de conversas anteriores    │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    BACKEND (Nuxt Server API)                    │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  POST /api/chat - Enviar mensagem                        │   │
│  │  1. Salva no Redis (cache 24h)                           │   │
│  │  2. Chama Python Agent (IA + Busca Web)                  │   │
│  │  3. Salva resposta no Redis                              │   │
│  │  4. Persiste tudo no PostgreSQL                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  GET /api/chat - Listar todas as conversas               │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  GET /api/chat/[id] - Carregar conversa específica       │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  DELETE /api/chat/[id] - Deletar conversa                │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
           │                    │                    │
           ▼                    ▼                    ▼
    ┌───────────┐        ┌───────────┐       ┌──────────────┐
    │   REDIS   │        │POSTGRESQL │       │ PYTHON AGENT │
    │  (Cache)  │        │ (Prisma)  │       │  (AgentOS)   │
    │  Port:    │        │  Port:    │       │  Port: 7777  │
    │   6379    │        │   5432    │       │              │
    │           │        │           │       │ - OpenAI GPT │
    │ TTL: 24h  │        │ Permanente│       │ - DuckDuckGo │
    └───────────┘        └───────────┘       └──────────────┘
```

---

## 🗄️ Schema do Banco de Dados

```prisma
model Conversa {
  id        String      @id @default(cuid())
  titulo    String
  mensagens Mensagem[]
  createdAt DateTime    @default(now())
  updatedAt DateTime    @updatedAt
}

model Mensagem {
  id          String    @id @default(cuid())
  conversaId  String
  conversa    Conversa  @relation(fields: [conversaId], references: [id], onDelete: Cascade)
  role        String
  content     String    @db.Text
  createdAt   DateTime  @default(now())
}
```

---

## 🔄 Fluxo de Dados

### 1️⃣ Usuário envia mensagem

```
Frontend → useSupraIA.sendMessage() → POST /api/chat
```

### 2️⃣ Backend processa

```
1. Salva mensagem do usuário no Redis
2. Chama Python Agent (http://supra-agent:7777)
3. Agent processa com GPT-4 + DuckDuckGo Search
4. Salva resposta no Redis
5. Persiste tudo no PostgreSQL (Prisma)
6. Retorna resposta para o frontend
```

### 3️⃣ Frontend exibe

```
Adiciona mensagem no array → Vue renderiza → Usuário vê resposta
```

---

## 📊 Interfaces Administrativas

### Prisma Studio
Interface visual moderna para PostgreSQL.

```bash
docker compose exec -d app bun prisma studio --hostname 0.0.0.0 --port 5555
open http://localhost:5555
```

**Funcionalidades:**
- ✅ Ver/Editar tabelas
- ✅ Filtros e buscas
- ✅ Adicionar/Deletar registros
- ✅ Ver relacionamentos

---

### PgAdmin
Admin completo para PostgreSQL.

```bash
open http://localhost:5050
```

**Login:** `admin@supraia.com` / `admin123`

**Configurar servidor:**
- Host: `localhost`
- Port: `5432`
- Database: `supradb`
- Username: `suprauser`
- Password: `suprapass`

**Funcionalidades:**
- ✅ SQL Query Tool
- ✅ Backup/Restore
- ✅ Gráficos e estatísticas
- ✅ Gerenciamento completo

---

### Redis Commander
Interface visual para Redis.

```bash
open http://localhost:8081
```

**Funcionalidades:**
- ✅ Ver todas as chaves
- ✅ Valores JSON formatados
- ✅ TTL (tempo de expiração)
- ✅ Deletar chaves

---

## 📈 Métricas do Projeto

- **Linhas de código:** ~2.000+
- **Componentes Vue:** 3
- **API Endpoints:** 4
- **Serviços Docker:** 6
- **Tecnologias:** 15+
- **Tempo de desenvolvimento:** 2 semanas

---

## 🎓 Aprendizados

Este projeto foi desenvolvido para demonstrar:

✅ **Arquitetura Full-Stack** - Frontend + Backend + Banco + Cache  
✅ **Integração de IA** - OpenAI GPT-4 com ferramentas customizadas  
✅ **Persistência de Dados** - Redis (cache) + PostgreSQL (permanente)  
✅ **DevOps** - Docker Compose com múltiplos serviços  
✅ **Boas Práticas** - TypeScript, Prisma ORM, API REST  
✅ **UI/UX Moderno** - Nuxt UI + Tailwind CSS  


---

## 👨‍💻 Autor

**Douglas Junior**

- 🌐 GitHub: [@dbribeiroo](https://github.com/dbribeiroo)
- 💼 LinkedIn: [douglas-junior](https://www.linkedin.com/in/douglas-j%C3%BAnior-6a77962a4/)
- 📧 Email: dbribeirogt@gmail.com
- 🌍 Localização: Vale do Aço, MG - Brasil

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

⭐ Se você gostou desse projeto, deixe uma estrela no GitHub!

[⬆ Voltar ao topo](#-supraia)

</div>
