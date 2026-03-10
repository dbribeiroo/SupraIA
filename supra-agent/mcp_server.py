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
                return f"ERRO CRÍTICO: O arquivo {nome_arquivo_real} foi lido, mas nao achei '{termo_busca}' dentro dele."
    except Exception as e:
        return f"ERRO CRÍTICO ao ler o arquivo: {str(e)}"


@mcp.tool()
def calcular_custo_cabo(distancia_metros: float, preco_metro: float) -> str:
    """
    Use esta ferramenta para calcular o custo total do cabo drop.
    ATENCAO: Voce DEVE usar a ferramenta 'consultar_preco_item' ANTES para descobrir o 'preco_metro' atualizado do 'CABO OPTICO DROP'.
    """
    dist = Decimal(str(distancia_metros))
    preco = Decimal(str(preco_metro))
    sobra_tecnica = Decimal('15.0') 
    metragem_total = dist + sobra_tecnica
    custo_total = metragem_total * preco
    return f"Metragem total (com {sobra_tecnica}m de sobra): {metragem_total}m. Custo total do cabo: R$ {custo_total:.2f}"


@mcp.tool()
def consultar_ficha_tecnica(modelo_equipamento: str) -> str:
    """
    Consulte esta ferramenta para descobrir as caracteristicas tecnicas de um equipamento (Wi-Fi, portas, limite de banda).
    Use ANTES de aprovar um orcamento para garantir que o equipamento suporta o plano de internet do cliente.
    """
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "fichas_tecnicas.csv")
    
    if not os.path.exists(caminho_arquivo):
        return "ERRO CRÍTICO: O arquivo fichas_tecnicas.csv nao foi encontrado no servidor."
        
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8', errors='ignore') as file:
            leitor_csv = csv.reader(file, delimiter=';') 
            resultados = []
            for linha in leitor_csv:
                linha_texto = " | ".join(linha).upper()
                if modelo_equipamento.upper() in linha_texto:
                    resultados.append(linha_texto)
            if resultados:
                return "ESPECIFICAÇÕES TÉCNICAS ENCONTRADAS:\n" + "\n".join(resultados)
            else:
                return f"Aviso: Nenhuma ficha tecnica encontrada para o modelo '{modelo_equipamento}'."
    except Exception as e:
        return f"ERRO CRÍTICO ao ler o arquivo de fichas: {str(e)}"


@mcp.tool()
def analisar_consumo_historico_plano(nome_plano: str) -> str:
    """
    Analisa o relatorio de consumo real do BI (Up Value/Voalle) para um plano especifico.
    Retorna a lista de produtos gastos, quantidades totais e o custo financeiro real daquele plano no periodo.
    """
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "historico_consumo.csv")
    
    if not os.path.exists(caminho_arquivo):
        return "ERRO CRÍTICO: O arquivo historico_consumo.csv nao foi encontrado."
        
    try:
        with open(caminho_arquivo, mode='r', encoding='utf-8', errors='ignore') as file:
            leitor_csv = csv.DictReader(file, delimiter=',')
            colunas = leitor_csv.fieldnames
            
            if not colunas:
                return "ERRO CRÍTICO: CSV vazio ou sem cabecalho."
                
            col_plano = next((c for c in colunas if "SERVI" in c.upper() or "CONTRATO" in c.upper()), None)
            col_produto = next((c for c in colunas if "PRODUTO" in c.upper()), None)
            col_quant = next((c for c in colunas if "QUANT" in c.upper()), None)
            col_valor = next((c for c in colunas if "VALOR" in c.upper()), None)
            
            if not all([col_plano, col_produto, col_quant, col_valor]):
                return f"ERRO CRÍTICO: Colunas nao encontradas no CSV. Cabecalho atual: {colunas}"
                
            consumo_produtos = {}
            valor_total_plano = Decimal('0.0')
            
            # Variáveis de diagnóstico
            planos_lidos = set()
            linhas_encontradas = 0
            erros_matematicos = 0
            
            for linha in leitor_csv:
                plano_linha = str(linha.get(col_plano, '')).strip().upper()
                if plano_linha:
                    planos_lidos.add(plano_linha)
                
                # Se o texto digitado pelo agente está contido na linha do arquivo
                if nome_plano.upper() in plano_linha:
                    linhas_encontradas += 1
                    produto = str(linha.get(col_produto, '')).strip()
                    qtd_str = str(linha.get(col_quant, '0')).replace('.', '').replace(',', '.')
                    valor_str = str(linha.get(col_valor, '0')).upper().replace('R$', '').replace('.', '').replace(',', '.').strip()
                    
                    try:
                        qtd = float(qtd_str) if qtd_str else 0.0
                        valor = Decimal(valor_str) if valor_str else Decimal('0.0')
                    except ValueError:
                        erros_matematicos += 1
                        continue 
                        
                    if produto not in consumo_produtos:
                        consumo_produtos[produto] = {'qtd': 0.0, 'valor': Decimal('0.0')}
                        
                    consumo_produtos[produto]['qtd'] += qtd
                    consumo_produtos[produto]['valor'] += valor
                    valor_total_plano += valor
                    
            if not consumo_produtos:
                amostra = list(planos_lidos)[:5]
                return (f"DIAGNÓSTICO DO SERVIDOR:\n"
                        f"Nenhum dado somado para '{nome_plano}'.\n"
                        f"- Linhas que bateram com o nome do plano: {linhas_encontradas}\n"
                        f"- Linhas puladas por erro na formatação do valor: {erros_matematicos}\n"
                        f"- Alguns planos que o Python conseguiu enxergar no arquivo: {amostra}")
                
            linhas_resposta = [f"📊 DADOS REAIS DE CONSUMO (BI) - PLANO: {nome_plano.upper()}"]
            linhas_resposta.append("-" * 50)
            produtos_ordenados = sorted(consumo_produtos.items(), key=lambda x: x[1]['valor'], reverse=True)
            
            for prod, dados in produtos_ordenados:
                linhas_resposta.append(f"Produto: {prod} | Quantidade Usada: {dados['qtd']} | Custo Historico: R$ {dados['valor']:.2f}")
                
            linhas_resposta.append("-" * 50)
            linhas_resposta.append(f"💰 CUSTO TOTAL DE MATERIAIS DESTE PLANO NO PERÍODO: R$ {valor_total_plano:.2f}")
            
            return "\n".join(linhas_resposta)
            
    except Exception as e:
        return f"ERRO CRÍTICO ao processar o historico: {str(e)}"
    
@mcp.tool()
def consultar_baseline_cac_supranet() -> str:
    """
    Retorna a base de calculo real do Custo de Aquisicao de Cliente (CAC) da Supranet,
    baseado no DRE de Jan-Ago de 2025.
    Use esta ferramenta SEMPRE que precisar calcular a viabilidade financeira ou o tempo 
    de retorno (Payback) de um novo cliente.
    """
    linhas_resposta = [
        "📊 BASE DE DADOS FINANCEIRA - SUPRANET (Referência: Jan-Ago 2025 - Ipatinga/MG)",
        "-" * 60,
        "- Total de Clientes Adquiridos no período: 5.336",
        "- CAC Médio Histórico Geral: R$ 970,96 por cliente.",
        "-" * 60,
        "💡 ESTRUTURA MATEMÁTICA PARA NOVOS ORÇAMENTOS (REGRA DE NEGÓCIO):",
        "O custo operacional FIXO de aquisição por cliente (Marketing, Comercial, Comissões e Salário das Equipes) é exatamente R$ 622,12.",
        "",
        "🛠️ INSTRUÇÃO DE CÁLCULO PARA O AGENTE:",
        "Para calcular o Custo de Aquisição (CAC) EXATO de um cliente novo, você DEVE somar:",
        "1. Custo Operacional Fixo: R$ 622,12",
        "2. Custo de Materiais do Plano: (Use a ferramenta 'analisar_consumo_historico_plano' para descobrir)",
        "3. Custo do Equipamento (ONU/Roteador): (Some o valor da ONU que será utilizada).",
        "",
        "FÓRMULA DO PAYBACK (Tempo de Retorno):",
        "Divida o CAC EXATO pelo valor da mensalidade do plano escolhido para descobrir em quantos meses o cliente se paga."
    ]
    
    return "\n".join(linhas_resposta)

if __name__ == "__main__":
    mcp.run(transport='stdio')