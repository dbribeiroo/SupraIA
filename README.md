<div align="center">

# 🚀 SupraIA

**Agente Inteligente da Supranet**

*Automatizando tarefas e facilitando o dia a dia dos colaboradores*

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Agno](https://img.shields.io/badge/Agno-AgentOS-purple.svg)](https://agno.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)](https://fastapi.tiangolo.com/)
[![Nuxt](https://img.shields.io/badge/Nuxt-4.x-00DC82.svg)](https://nuxt.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Sobre](#-sobre) • [Funcionalidades](#-funcionalidades) • [Tecnologias](#-tecnologias) • [Roadmap](#-roadmap) • [Como Rodar](#-como-rodar) • [Arquitetura](#-arquitetura)

</div>

---

## 📖 Sobre

**SupraIA** é um agente inteligente desenvolvido para a **Supranet** (provedor de internet fibra óptica do Vale do Aço - MG). O Supra é o mascote da empresa transformado em um assistente virtual que integra com os sistemas internos para:

- ✅ Auxiliar colaboradores em suas tarefas diárias
- ✅ Responder dúvidas sobre processos e sistemas
- ✅ Automatizar tarefas repetitivas
- ✅ Buscar informações atualizadas na web
- ✅ Facilitar o acesso a dados da empresa

O projeto utiliza **IA generativa** (GPT-4) combinada com **ferramentas customizadas** para criar um assistente contextualizado e eficiente.

---

## ✨ Funcionalidades

### 🎯 Implementadas

- [x] **Busca Web em Tempo Real** - Busca informações atualizadas (cotações, notícias, clima)
- [x] **API REST** - Endpoints para integração com frontend e outros sistemas
- [x] **Interface Web** - Chat interativo desenvolvido em Nuxt 4 + Vue 3
- [x] **Containerização** - Deploy facilitado com Docker
- [x] **Personalidade Customizada** - Responde como o mascote Supra 🚀

### 🔄 Em Desenvolvimento

- [ ] **Memória Persistente** - Mantém histórico de conversas (SQLite)
- [ ] **Integração com CRM** - Consultar dados de clientes
- [ ] **Sistema de Tickets** - Criar e consultar chamados
- [ ] **Base de Conhecimento** - RAG com documentação interna
- [ ] **Relatórios Automatizados** - Gerar relatórios de vendas/suporte
- [ ] **Notificações** - Alertas via WhatsApp/Email
- [ ] **Dashboard Analytics** - Métricas de uso do agente

---

## 🛠️ Tecnologias

### Backend (Agente IA)

| Tecnologia | Descrição |
|------------|-----------|
| **Python 3.12** | Linguagem principal |
| **Agno AgentOS** | Framework para agentes IA |
| **OpenAI GPT-4o-mini** | Modelo de linguagem |
| **FastAPI** | API REST de alta performance |
| **SQLite** | Banco de dados para memória |
| **DDGS** | Busca web multi-backend |

### Frontend

| Tecnologia | Descrição |
|------------|-----------|
| **Nuxt 4** | Framework Vue.js full-stack |
| **Vue 3** | Framework JavaScript reativo |
| **Bun** | Runtime JavaScript moderno |
| **TailwindCSS** | Framework CSS utility-first |
| **TypeScript** | Tipagem estática |

### DevOps

- **Docker** + **Docker Compose** - Containerização
- **uv** - Gerenciador de pacotes Python moderno
- **Git** - Controle de versão

---

## 🚀 Como Rodar

### Pré-requisitos

- Docker e Docker Compose instalados
- Chave de API da OpenAI

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/supraIA.git
cd supraIA
```

### 2️⃣ Configure as variáveis de ambiente

```bash
# Backend (supra-agent/.env)
echo "OPENAI_API_KEY=sua-chave-aqui" > supra-agent/.env

# Frontend (.env)
cp .env.example .env
```

### 3️⃣ Suba os containers

```bash
docker-compose up --build
```

### 4️⃣ Acesse a aplicação

- **Frontend:** [http://localhost:3000](http://localhost:3000)
- **API Docs:** [http://localhost:7777/docs](http://localhost:7777/docs)

---

## 🏗️ Arquitetura

```
┌─────────────────────────────────────────────────────────────┐
│                         FRONTEND                            │
│                    Nuxt 4 + Vue 3 + Bun                     │
│                    (Interface do Chat)                      │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTP/REST
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                      BACKEND (API)                          │
│                   FastAPI + Agno AgentOS                    │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              SUPRA AGENT (GPT-4o-mini)                │  │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐       │  │
│  │  │ Web Search │  │   Memory   │  │   Tools    │       │  │
│  │  │   (DDGS)   │  │  (SQLite)  │  │  (Custom)  │       │  │
│  │  └────────────┘  └────────────┘  └────────────┘       │  │
│  └─────────────────────────────────────────────────────-─┘  │
└────────────────────┬────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────┐
│                  INTEGRAÇÕES FUTURAS                        │
│   CRM  │  Tickets  │  WhatsApp  │  Email  │  Banco de Dados │
└─────────────────────────────────────────────────────────────┘
```

---

## 📂 Estrutura do Projeto

```
supraIA/
├── app/                    # Frontend Nuxt
│   ├── components/         # Componentes Vue
│   ├── pages/              # Páginas da aplicação
│   └── composables/        # Lógica reutilizável
│
├── supra-agent/            # Backend Python (Agente IA)
│   ├── agent.py            # Configuração do agente
│   ├── pyproject.toml      # Dependências Python
│   ├── Dockerfile          # Container do backend
│   └── .env                # Variáveis de ambiente
│
├── docker-compose.yml      # Orquestração dos containers
├── nuxt.config.ts          # Configuração do Nuxt
└── README.md               # Este arquivo
```

---

## 🗺️ Roadmap

### Fase 1: MVP ✅ (Concluída)
- [x] Agente básico com GPT-4
- [x] Busca web em tempo real
- [x] Interface de chat
- [x] Deploy com Docker

### Fase 2: Integrações 🔄 (Em andamento)
- [ ] Integração com CRM da Supranet
- [ ] Sistema de tickets
- [ ] Base de conhecimento (RAG)
- [ ] Autenticação de usuários

### Fase 3: Automações 📅 (Planejado)
- [ ] Relatórios automatizados
- [ ] Notificações WhatsApp/Email
- [ ] Agendamento de tarefas
- [ ] Dashboard de analytics

### Fase 4: Escalabilidade 🚀 (Futuro)
- [ ] Deploy em produção (Railway/AWS)
- [ ] Multi-tenancy (suporte a múltiplas empresas)
- [ ] API pública para parceiros
- [ ] App mobile (React Native)

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 👨‍💻 Autor

**Douglas Junior**

- GitHub: [@dbribeiroo](https://github.com/dbribeiroo)
- LinkedIn: www.linkedin.com/in/douglas-j%C3%BAnior-6a77962a4/
- Email: dbribeirogt@gmail.com

---

<div align="center">

**Feito com ❤️ para a Supranet** 🚀

</div>
