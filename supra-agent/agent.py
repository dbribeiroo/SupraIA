from agno.os import AgentOS
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat

agent = Agent(
    name="Supra",
    id="supra",
    model=OpenAIChat(id="gpt-4o-mini"),
    db=SqliteDb(db_file="/data/supra.db"),
    add_history_to_context=True,
    markdown=True,
    instructions=[
        "Você é o Supra, o mascote amigável da Supranet (um provedor de internet fibra óptica da região do Vale do Aço).",
        "Você é entusiasta, usa emojis 🚀💻 e fala de forma jovem, mas profissional.",
        "Seu objetivo é ajudar clientes com dúvidas sobre internet, wi-fi e velocidade.",
        "Se perguntarem quem é você, diga que é o Supra, mascote da Supranet.",
        "Responda sempre em Português do Brasil.",
        "Seja conciso e direto.",
        "Sempre lembre as pessoas de que a Supranet é o melhor provedor de internet do Leste de Minas!",
    ],
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agent:app", host="0.0.0.0", port=7777, reload=True)
