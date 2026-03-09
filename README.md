<div align="center">

# 🚀 SupraIA

**Corporate AI Platform**

*Sistema projetado para resolver problemas reais de telecomunicações*

[![Nuxt](https://img.shields.io/badge/Nuxt-4.x-00DC82.svg)](https://nuxt.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791.svg)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/Redis-7-DC382D.svg)](https://redis.io/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Sobre](#-sobre) • [Funcionalidades](#-funcionalidades) • [Tecnologias](#-tecnologias) • [Como Rodar](#-como-rodar) • [Arquitetura](#-arquitetura) • [Interfaces](#-interfaces-administrativas)

</div>

---

## 📖 Sobre

**SupraIA** não é apenas um chat, é uma **Plataforma de Agentes de IA Corporativos** focada na automação de processos críticos de telecomunicações. O sistema utiliza uma arquitetura moderna e desacoplada que combina:

- 🤖 **Arquitetura Baseada em Agentes (AgentOS)**: IA Generativa orquestrada para tomada de decisões lógicas.
- 🔌 **Model Context Protocol (MCP)**: Servidor de ferramentas isolado, garantindo segurança, escalabilidade e compartilhamento de funções (como cálculos financeiros e leitura de dados) entre múltiplos agentes.
- 📊 **Integração de Dados Locais**: Leitura dinâmica de tabelas de preços para geração de orçamentos precisos em tempo real.
- 💾 **Persistência Dupla e Cache**: PostgreSQL + Prisma ORM para dados permanentes e Redis para cache ultra-rápido de mensagens.
- 🎨 **Interface Corporativa**: Frontend reativo com Nuxt 4 + Vue 3 + Nuxt UI.
- 🐳 **Infraestrutura Escalável**: Containerização completa com Docker Compose 

O projeto foi desenvolvido como portfólio profissional, demonstrando habilidades em:
- Arquitetura de Microsserviços e Protocolo MCP
- Automação de Regras de Negócio e Cálculos Financeiros (Viabilidade de Rede)
- Integração Frontend/Backend com gerenciamento avançado de estado
- DevOps, Containerização e ferramentas administrativas (Prisma Studio, PgAdmin)

---

## ✨ Funcionalidades

### 🎯 Implementadas

- [x] **Agente Engenheiro de Custos** - IA especializada em calcular viabilidade de infraestrutura de fibra óptica.
- [x] **Servidor MCP Isolado** - Separação da lógica de ferramentas (músculos) do motor de IA (cérebro), permitindo escalabilidade.
- [x] **Motor de Cálculo Financeiro** - Processamento de custos de cabeamento e sobra técnica com precisão bancária.
- [x] **Extração de Dados Locais** - Leitura e busca de equipamentos em arquivos CSV de estoque integrados à IA.
- [x] **Busca Web em Tempo Real** - DuckDuckGo Search integrado para contexto externo.
- [x] **Histórico de Conversas** - Sidebar com lista de conversas anteriores e CRUD completo.
- [x] **Persistência Dupla** - Redis (cache 24h) + PostgreSQL (permanente).
- [x] **Interface Responsiva** - Design moderno com formatação dinâmica de tabelas de orçamento via Nuxt UI + Tailwind.
- [x] **API REST** - Endpoints documentados para comunicação entre Nuxt e Python.

### 🔄 Próximas Melhorias (Roadmap Multi-Agentes)

- [ ] **Orquestrador de Agentes** - Sistema de roteamento inteligente que direciona a dúvida do usuário para o especialista correto.
- [ ] **Agente de Customer Success / Suporte** - Novo especialista focado em retenção de clientes e troubleshooting técnico.
- [ ] **Agente Comercial** - Especialista focado em vendas e planos de internet, compartilhando o mesmo Servidor MCP.
- [ ] **Autenticação** - Sistema de login com isolamento de histórico por usuário/setor.
- [ ] **Streaming de Respostas** - Experiência de digitação fluida em tempo real (SSE).
- [ ] **Integração com ERP (SGP/IXC)** - Conectar o servidor MCP diretamente ao banco de dados do provedor.

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
| **Python** | 3.12 | Linguagem principal do ecossistema de IA |
| **Agno (AgentOS)** | Latest | Framework de orquestração para agentes IA |
| **FastMCP** | Latest | Servidor local para Model Context Protocol (stdio) |
| **uv** | Latest | Gerenciador de pacotes e ambientes virtuais ultra-rápido |
| **OpenAI API** | GPT-4mini | Motor cognitivo e processamento de linguagem |
| **DuckDuckGo** | 8.x | Ferramenta de busca web em tempo real |
| **Nuxt Server** | 4.x | API Routes para comunicação com o frontend |
| **Bun** | Latest | Runtime JavaScript moderno para o backend Node |

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

```text
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
│  │  2. Chama Motor de IA (Agent + MCP)                      │   │
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
    ┌───────────┐        ┌───────────┐       ┌──────────────────────────────────────────┐
    │   REDIS   │        │POSTGRESQL │       │           MOTOR DE IA (Python)           │
    │  (Cache)  │        │ (Prisma)  │       │                                          │
    │  Port:    │        │  Port:    │       │  ┌──────────────┐      ┌──────────────┐  │
    │   6379    │        │   5432    │       │  │ PYTHON AGENT │      │  MCP SERVER  │  │
    │           │        │           │       │  │  (AgentOS)   │<─┬──>│  (FastMCP)   │  │
    │ TTL: 24h  │        │ Permanente│       │  │  Port: 7777  │  │   │  Background  │  │
    └───────────┘        └───────────┘       │  │ - Orquestrar │stdio │ - Ler CSV    │  │
                                             │  │ - OpenAI GPT │  │   │ - Calc Mat.  │  │
                                             │  │ - DuckDuckGo │  │   │ - APIs Locais│  │
                                             │  └──────────────┘  │   └──────────────┘  │
                                             └────────────────────┴─────────────────────┘

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
1. Salva mensagem do usuário no Redis (Cache de sessão).
2. Chama Motor de IA (http://supra-agent:7777).
3. Agente analisa a intenção (Raciocínio):
   - Se precisar de contexto externo: Usa DuckDuckGo Search.
   - Se precisar de dados de estoque/preços: Chama Servidor MCP (mcp_server.py).
4. Servidor MCP executa a lógica local e retorna dados precisos ao Agente.
5. Agente consolida a resposta final.
6. Salva resposta no Redis e persiste no PostgreSQL via Prisma.
7. Retorna resposta formatada (Markdown) para o frontend.

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

- **Arquitetura:** Multi-Agent System (MAS) com suporte a MCP.
- **Linhas de código:** ~3669 linhas.
- **Componentes Vue:** 3
- **API Endpoints:** 4
- **Serviços Docker:** 6
- **Protocolos de IA:** Model Context Protocol (MCP) via stdio.
- **Tempo de resposta (Cache):** < 50ms (Redis).
- **Tecnologias:** 17+ (Nuxt 4, Vue 3, Python 3.12, Agno, FastMCP, Docker, Prisma, etc.).
- **Tempo de desenvolvimento:** 1 mês.

---

## 🎓 Aprendizados Técnicos

Este projeto foi desenvolvido para demonstrar:

- ✅ **Arquitetura de Agentes (MAS)** – Implementação de um sistema multi-agente (*Multi-Agent System*) com orquestração de especialistas dedicados.
- ✅ **Model Context Protocol (MCP)** – Integração do protocolo de contexto mais moderno do mercado para desacoplar o raciocínio da IA das ferramentas operacionais via `stdio`.
- ✅ **Engenharia de Prompt e Redução de Alucinações** – Uso de ferramentas customizadas (*Tool Use*) para garantir que a IA utilize dados reais de estoque e cálculos matemáticos precisos em vez de estimativas genéricas.
- ✅ **DevOps & Resiliência** – Gerenciamento e orquestração de 6 serviços simultâneos em Docker Compose, garantindo isolamento de rede e persistência de dados.
- ✅ **Estratégia de Persistência Híbrida** – Implementação de cache de alta performance com Redis (TTL 24h) e armazenamento relacional permanente com PostgreSQL e Prisma ORM.
- ✅ **Desenvolvimento Full-Stack Nuxt 4** – Construção de uma interface reativa moderna com TypeScript, focada na experiência do usuário corporativo.

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
