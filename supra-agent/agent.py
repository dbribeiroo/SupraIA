from agno.os import AgentOS
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.tools.websearch import WebSearchTools 

TABELA_PRECOS = {
    "cabo_drop": {
        "descricao": "Cabo Óptico Drop Flat (Preço por metro)",
        "novo": 1.25,
        "reuso": 1.25 
    },
    "onu_bridge": {
        "descricao": "ONU Bridge Básica",
        "novo": 120.00,
        "reuso": 35.00 
    },
    "roteador_wifi6": {
        "descricao": "Roteador Wi-Fi 6 (Padrão 400mb)",
        "novo": 280.00,
        "reuso": 70.00
    },
    "mao_de_obra": {
        "descricao": "Custo da hora técnica (Técnico + Veículo)",
        "novo": 55.00, # Valor da hora
        "reuso": 55.00
    }
}

def consultar_preco_item(item_id: str, estado: str = "novo") -> str:
    """
    Use esta ferramenta SEMPRE que precisar saber o custo de um equipamento, material ou mão de obra.
    
    Args:
        item_id: O identificador do item (ex: 'cabo_drop', 'onu_bridge', 'roteador_wifi6', 'mao_de_obra').
        estado: O estado do item, pode ser 'novo' ou 'reuso'. Padrão é 'novo'.
        
    Returns:
        O valor do item formatado em Reais (R$) ou uma mensagem de erro se o item não existir.
    """
    item = TABELA_PRECOS.get(item_id)
    
    if not item:
        return f"Erro: O item '{item_id}' não foi encontrado na tabela de preços. Verifique os itens disponíveis."
    
    preco = item.get(estado)
    if preco is None:
        return f"Erro: Estado '{estado}' não é válido para o item '{item_id}'."
        
    return f"O custo do item {item['descricao']} ({estado}) é R$ {preco:.2f}"

def calcular_custo_cabo(distancia_metros: float) -> str:
    """
    Use esta ferramenta SEMPRE que precisar calcular o custo do cabo drop baseado na distância.
    
    Args:
        distancia_metros: A distância estimada em metros da CTO (poste) até a casa do cliente.
        
    Returns:
        O valor total do cabo calculado em Reais (R$), incluindo a sobra técnica.
    """
    preco_metro = TABELA_PRECOS["cabo_drop"]["novo"]
    
    sobra_tecnica = 15.0
    metragem_total = distancia_metros + sobra_tecnica
    
    custo_total = metragem_total * preco_metro
    
    return f"Distância informada: {distancia_metros}m. Metragem total com sobra técnica ({sobra_tecnica}m): {metragem_total}m. Custo total do cabo: R$ {custo_total:.2f}"

agent = Agent(
    name="Supra",
    id="supra",
    model=OpenAIChat(id="gpt-4o-mini"),
    db=SqliteDb(db_file="/data/supra.db"),
    update_memory_on_run=True,
    
    tools=[WebSearchTools(backend="auto"), consultar_preco_item, calcular_custo_cabo], 
    
    add_history_to_context=True,
    markdown=True,
    instructions=[
        "Você é o Supra, o engenheiro de viabilidade e custos da Supranet.",
        "Seu objetivo é calcular com precisão de centavos o custo de instalação de internet para a empresa.",
        "NUNCA invente preços de equipamentos ou cabos. SEMPRE use a ferramenta 'consultar_preco_item' para descobrir o valor atualizado.",
        "Para calcular o custo de cabeamento, SEMPRE use a ferramenta 'calcular_custo_cabo' informando a distância.",
        "Quando perguntado sobre um custo, detalhe os itens (Cabo, ONU, Mão de obra), mostre o valor unitário de cada um, e depois o custo total.",
        "Diferencie claramente quando um equipamento é 'novo' ou de 'reuso', pois isso afeta o lucro da empresa.",
        "Seja profissional, analítico e use tabelas em Markdown para apresentar o orçamento final.",
        "## IMPORTANTE: USO DE FERRAMENTAS",
        "SEMPRE que o usuário perguntar sobre notícias atuais, cotação de moedas ou clima, você DEVE usar a ferramenta 'Web Search'.",
        "Se perguntarem quem é você, diga que é o Supra, mascote da Supranet e analista de custos.",
        "Responda sempre em Português do Brasil.",
    ],
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agent:app", host="0.0.0.0", port=7777, reload=True)