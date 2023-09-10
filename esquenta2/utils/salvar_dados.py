import os
import csv

def salvarInformacoes(dados, caminhoAbsoluto, pasta, nomeArquivo='dados.csv'):
    if not os.path.exists(pasta):
        os.makedirs(pasta)

    caminho_completo = os.path.join(caminhoAbsoluto, pasta, nomeArquivo)

    with open(caminho_completo, 'w', newline='') as arquivo:
        # Defina as colunas manualmente com base no formato dos dados
        colunas = ['Iteracao', 'Tempo de Execucao (s)', 'Uso de Memoria - atual (MB)', 'Uso de Memoria - Pico (MB)']

        escritor_csv = csv.DictWriter(arquivo, fieldnames=colunas)
        escritor_csv.writeheader()

        for i, linha in dados.items():
            # Extrai os valores diretamente com base nas chaves
            escritor_csv.writerow({
                'Iteracao': i,
                'Tempo de Execucao (s)': linha['Tempo de Execucao (s)'],
                'Uso de Memoria - atual (MB)': linha['Uso de Memoria - atual (MB)'],
                'Uso de Memoria - Pico (MB)': linha['Uso de Memoria - Pico (MB)'],
            })

    print(f'Dados salvos em {caminho_completo}')
