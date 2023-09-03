import pandas as pd
import csv
import numpy as np 
import matplotlib.pyplot as plt
import os
from utils.arguments_parser import parser_arguments_medias
from utils.dicionarios_utilizados import dicionarios_utilizados

def getCaminhoOutput(pasta, algoritmo):
    caminho_relativo = os.path.join(pasta, 'output',algoritmo)
    return caminho_relativo


def medias(caminho_arquivo):
    nome_arquivo = 'dados.csv'
    caminho_arquivo = os.path.join(caminho_arquivo, nome_arquivo)
    df = pd.read_csv(caminho_arquivo)

    media_memoria = df['Uso de Memoria - Pico (MB)'].mean()
    media_tempo = df['Tempo de Execucao (s)'].mean()

    return media_memoria, media_tempo


def salvar_dados(tipo, seu_dicionario, alg):
    # Caminho do arquivo CSV
    nome_arquivo_tempo = f'mediasTempo_{tipo}_{alg}.csv'
    nome_arquivo_memoria = f'mediasMemoria_{tipo}_{alg}.csv'
    # Caminhos dos arquivos CSV para tempo e memória
    caminho_arquivo_csv_tempo = os.path.join('mediaExecucao', nome_arquivo_tempo)
    caminho_arquivo_csv_memoria = os.path.join('mediaMemoria', nome_arquivo_memoria)

    
    # Abrir os arquivos CSV para escrita (tempo)
    with open(caminho_arquivo_csv_tempo, 'w', newline='') as arquivo_csv_tempo:
        escritor_csv_tempo = csv.writer(arquivo_csv_tempo)

        # Escrever os cabeçalhos das colunas (algoritmos e tamanhos)
        cabecalho_tempo = ['algoritmos'] + list(seu_dicionario[list(seu_dicionario.keys())[0]].keys())
        escritor_csv_tempo.writerow(cabecalho_tempo)

        # Iterar sobre as chaves do dicionário para escrever os dados de tempo nas linhas
        for algoritmo, dados in seu_dicionario.items():
            linha_tempo = [algoritmo] + [dados[tamanho]['tempo'] for tamanho in cabecalho_tempo[1:]]
            escritor_csv_tempo.writerow(linha_tempo)

    # Abrir o arquivo CSV para escrita (memória)
    with open(caminho_arquivo_csv_memoria, 'w', newline='') as arquivo_csv_memoria:
        escritor_csv_memoria = csv.writer(arquivo_csv_memoria)

        # Escrever os cabeçalhos das colunas (algoritmos e tamanhos)
        cabecalho_memoria = ['algoritmos'] + list(seu_dicionario[list(seu_dicionario.keys())[0]].keys())
        escritor_csv_memoria.writerow(cabecalho_memoria)

        # Iterar sobre as chaves do dicionário para escrever os dados de memória nas linhas
        for algoritmo, dados in seu_dicionario.items():
            linha_memoria = [algoritmo] + [dados[tamanho]['memoria'] for tamanho in cabecalho_memoria[1:]]
            escritor_csv_memoria.writerow(linha_memoria)

def main():
    print('Iniciando ...')
    args = parser_arguments_medias()
    dicionarios = dicionarios_utilizados()

    tipo_lista = dicionarios['t'][args.t]

    if args.a == 'a':
        pasta = 'buscaLinearV1'
    elif args.a == 'b':
        pasta = 'buscaLinearV2'
    elif args.a == 'c':
        pasta = 'buscaBinaria'
    elif args.a == 'd':
        pasta = 'buscaQuadratica'
    elif args.a == 'e':
        pasta = 'buscaTernaria'
    elif args.a == 'f':
        pasta = 'buscaCubica'


    dicionario_alg = {}
    dicionario_resultado = {}
    diretorio_base = getCaminhoOutput(pasta=pasta, algoritmo=args.a)
    for subdiretorio in os.listdir(diretorio_base):
        if subdiretorio.isdigit():
            caminho_arquivo = os.path.join(diretorio_base, subdiretorio, tipo_lista)
            array_memoria = []
            array_tempo = []
            if os.path.exists(caminho_arquivo):
                for sub_subdir in os.listdir(caminho_arquivo):
                    caminho_completo = os.path.join(caminho_arquivo, sub_subdir)
                    
                    memoria, tempo = medias(caminho_arquivo=caminho_completo)
                    array_memoria.append(memoria)
                    array_tempo.append(tempo)

                array_memoria = np.array(array_memoria)
                array_tempo = np.array(array_tempo)
                media_memoria = np.mean(array_memoria)
                media_tempo = np.mean(array_tempo)
                dicionario_resultado[subdiretorio] = {
                    'tempo': media_tempo,
                    'memoria': media_memoria
                }

            else:
                print('Caminho Não Existe: ', caminho_arquivo)

    chaves_ordenadas = sorted(dicionario_resultado.keys(), key=lambda x: int(x))

    resultado_ordenado={}

    # Agora "chaves_ordenadas" conterá as chaves numéricas em ordem
    for chave in chaves_ordenadas:
        valor = dicionario_resultado[chave]
        resultado_ordenado[chave] = valor

    dicionario_alg[dicionarios['a'][args.a]] = resultado_ordenado

    salvar_dados(tipo=args.t, seu_dicionario=dicionario_alg, alg=args.a)
    print('Concluido !!')

if __name__ == "__main__":
    main()