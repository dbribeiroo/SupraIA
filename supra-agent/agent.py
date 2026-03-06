from agno.os import AgentOS
from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.openai import OpenAIChat
from agno.tools.websearch import WebSearchTools 
import csv
import os

def consultar_preco_item(termo_busca: str) -> str:

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    arquivos_na_pasta = os.listdir(diretorio_atual)
    
    nome_arquivo_real = None
    for arquivo in arquivos_na_pasta:
        if "tabela_precos" in arquivo.lower() and "csv" in arquivo.lower():
            nome_arquivo_real = arquivo
            break
            
    if not nome_arquivo_real:
        return f"ERRO CRÍTICO: Nenhum arquivo CSV encontrado. A pasta tem: {arquivos_na_pasta}"
        
    caminho_arquivo = os.path.join(diretorio_atual, nome_arquivo_real)
    
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8', errors='ignore') as file:
            leitor_csv = csv.reader(file, delimiter=';') 
            
            resultados = []
            for linha in leitor_csv:
                linha_texto = " | ".join(linha).upper()
                if termo_busca.upper() in linha_texto:
                    resultados.append(linha_texto)
                    
            if resultados:
                return "DADOS ENCONTRADOS NO BANCO:\n" + "\n".join(resultados[:10])
            else:
                return f"ERRO CRÍTICO: O arquivo {nome_arquivo_real} foi lido, mas não achei '{termo_busca}' dentro dele. (Tente mudar o delimiter para ',')"
                
    except Exception as e:
        return f"ERRO CRÍTICO ao ler o arquivo: {str(e)}"

def calcular_custo_cabo(distancia_metros: float, preco_metro: float) -> str:
    """
    Use esta ferramenta para calcular o custo total do cabo drop.
    ATENÇÃO: Você DEVE usar a ferramenta 'consultar_preco_item' ANTES para descobrir o 'preco_metro' atualizado do 'CABO OPTICO DROP'.
    
    Args:
        distancia_metros: A distância da CTO até a casa (em metros).
        preco_metro: O valor unitário do metro do cabo (use ponto para decimais, ex: 0.38).
    """
    sobra_tecnica = 15.0
    metragem_total = distancia_metros + sobra_tecnica
    
    custo_total = metragem_total * preco_metro
    
    return f"Metragem total (com {sobra_tecnica}m de sobra): {metragem_total}m. Custo total do cabo: R$ {custo_total:.2f}"

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
        "Se a ferramenta retornar uma mensagem começando com 'ERRO CRÍTICO', você DEVE exibir essa mensagem EXATAMENTE como está para o usuário, sem esconder ou alterar nenhuma palavra.",
        "Ao consultar a base de dados de preços, utilize SEMPRE e APENAS o 'Valor Unit.' para os cálculos de orçamento.",
        "NUNCA utilize o 'Valor Total' nas contas, pois ele representa o custo do estoque inteiro da empresa.",
    ],
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="agent:app", host="0.0.0.0", port=7777, reload=True)