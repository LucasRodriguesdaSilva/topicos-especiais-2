import os
import csv

def salvarInformacoes(dicionario,caminhoAbsoluto, pasta):
    nomeArquivo = 'dados.csv'
    caminho_completo = os.path.join(caminhoAbsoluto, pasta, nomeArquivo)

    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    with open(caminho_completo, 'w', newline='') as arquivo:
        colunas = ["Iteracao", "Uso de Memoria - Inicial (bytes)", 'Uso de Memoria - Final (bytes)', 'Uso de Memoria - Diferenca (bytes)', "Tempo de Execucao (s)", "Valor Procurado", "Indice no Vetor"] 
        escritor_csv = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor_csv.writeheader()
        
        for iteracao, dados in dicionario.items():
            escritor_csv.writerow({
                "Iteracao": iteracao,
                "Uso de Memoria - Inicial (bytes)": dados["uso_inicial"],
                "Uso de Memoria - Final (bytes)": dados["uso_final"],
                "Uso de Memoria - Diferenca (bytes)": dados["uso_diferenca"],
                "Tempo de Execucao (s)": dados["tempo_execucao"],
                "Valor Procurado": dados['valor_procurado'] , 
                "Indice no Vetor": dados['resultado_encontrado']
            })

    print(f'Dados salvos em {caminho_completo}')
