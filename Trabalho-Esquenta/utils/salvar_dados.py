import os
import csv

def salvarInformacoes(dicionario,caminhoAbsoluto, pasta):
    nomeArquivo = 'dados.csv'
    caminho_completo = os.path.join(caminhoAbsoluto, pasta, nomeArquivo)

    if not os.path.exists(pasta):
        os.makedirs(pasta)
    
    with open(caminho_completo, 'w', newline='') as arquivo:
        colunas = ["Iteracao", "Uso de Memoria - atual (MB)", 'Uso de Memoria - Pico (MB)', "Tempo de Execucao (s)", "X", "Indice"] 
        escritor_csv = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor_csv.writeheader()
        
        for iteracao, dados in dicionario.items():
            escritor_csv.writerow({
                colunas[0]: iteracao,
                colunas[1]: dados["uso_atual"],
                colunas[2]: dados["uso_pico"],
                colunas[3]: dados["tempo_execucao"],
                colunas[4]: dados['valor_procurado'] , 
                colunas[5]: dados['resultado_encontrado']
            })

    print(f'Dados salvos em {caminho_completo}')
