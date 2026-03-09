import csv
import os
from decimal import Decimal
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Supranet-MCP")

@mcp.tool()
def consultar_preco_item(termo_busca: str) -> str:
    """Busca um termo dentro do arquivo CSV de precos e retorna os resultados encontrados."""
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
                return f"ERRO CRÍTICO: O arquivo {nome_arquivo_real} foi lido, mas nao achei '{termo_busca}' dentro dele. (Tente mudar o delimiter para ',')"
                
    except Exception as e:
        return f"ERRO CRÍTICO ao ler o arquivo: {str(e)}"

@mcp.tool()
def calcular_custo_cabo(distancia_metros: float, preco_metro: float) -> str:
    """
    Use esta ferramenta para calcular o custo total do cabo drop.
    ATENCAO: Voce DEVE usar a ferramenta 'consultar_preco_item' ANTES para descobrir o 'preco_metro' atualizado do 'CABO OPTICO DROP'.
    
    Args:
        distancia_metros: A distancia da CTO ate a casa (em metros).
        preco_metro: O valor unitario do metro do cabo (use ponto para decimais, ex: 0.38).
    """
    dist = Decimal(str(distancia_metros))
    preco = Decimal(str(preco_metro))
    
    sobra_tecnica = Decimal('15.0') 
    
    metragem_total = dist + sobra_tecnica
    custo_total = metragem_total * preco
    
    return f"Metragem total (com {sobra_tecnica}m de sobra): {metragem_total}m. Custo total do cabo: R$ {custo_total:.2f}"

if __name__ == "__main__":
    mcp.run(transport='stdio')