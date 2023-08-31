import pandas as pd
import matplotlib.pyplot as plt
import os
from utils.arguments_parser import parser_arguments_plot
from utils.dicionarios_utilizados import dicionarios_utilizados

# camminho_absoluto = os.path.dirname(os.path.abspath(__file__))
def plotar_uso_memmoria(df, pasta_saida):
     # Calcular a média do Uso de Memória - Inicial
    media_memoria_inicial = df['Uso de Memoria - Inicial (bytes)'].mean() / (1024 ** 2)

    largura_polegadas = 8
    altura_polegadas = 6

    # Cria a figura com o tamanho especificado
    fig, ax = plt.subplots(figsize=(largura_polegadas, altura_polegadas))

    # Plotar gráfico de linha para Uso de Memória
    plt.plot(df['Iteracao'], df['Uso de Memoria - Inicial (bytes)'], label='Inicial', marker='o')
    plt.plot(df['Iteracao'], df['Uso de Memoria - Final (bytes)'], label='Final', marker='x')
    plt.plot(df['Iteracao'], df['Uso de Memoria - Diferenca (bytes)'], label='Diferença', marker='.')
    plt.axhline(y=media_memoria_inicial, color='r', linestyle='--', label=f'Média: {media_memoria_inicial:.2f} Megabytes')
    plt.xlabel('Iteração')
    plt.ylabel('Uso de Memória (bytes)')
    plt.title('Uso de Memória')
    plt.legend()
    plt.xticks(df['Iteracao'][::1], df['Iteracao'][::1], rotation=45) 
    plt.tight_layout()
    caminho_imagem = os.path.join(pasta_saida, 'uso_memoria.png')
    # Salvar o gráfico em um arquivo PNG
    plt.savefig(caminho_imagem)
    plt.close()

def plotar_tempo_execucao(df, pasta_saida):
    media_tempo_execucao = df['Tempo de Execucao (s)'].mean()

    # Define o tamanho da figura em polegadas
    largura_polegadas = 8
    altura_polegadas = 6

    # Cria a figura com o tamanho especificado
    fig, ax = plt.subplots(figsize=(largura_polegadas, altura_polegadas))

    # Plotar gráfico de linha para Tempo de Execução
    plt.plot(df['Iteracao'], df['Tempo de Execucao (s)'], marker='o')
    plt.axhline(y=media_tempo_execucao, color='r', linestyle='--', label=f'Média: {media_tempo_execucao:.2f} segundos')
    plt.xlabel('Iteração')
    plt.ylabel('Tempo de Execução (s)')
    plt.title('Gráfico de Linha - Tempo de Execução')
    plt.legend()
    plt.xticks(df['Iteracao'][::1], df['Iteracao'][::1], rotation=45) 
    plt.tight_layout()

    caminho_imagem = os.path.join(pasta_saida, 'tempo_execucao.png')
    # Salvar o gráfico em um arquivo PNG
    plt.savefig(caminho_imagem)

    # Fechar a figura para evitar sobreposição em iterações posteriores
    plt.close()

def getCaminhoOutput(pasta, algoritmo):
    caminho_relativo = os.path.join(pasta, 'output',algoritmo)
    return caminho_relativo


def plotar_imagem(caminho_arquivo):
    caminho = caminho_arquivo
    nome_arquivo = 'dados.csv'
    pasta_saida = os.path.join(caminho,'imagens')

    caminho_arquivo = os.path.join(caminho_arquivo, nome_arquivo)
    print('Lendo Arquivo no Caminho: ', caminho_arquivo)
    df = pd.read_csv(caminho_arquivo)

    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    print('Salvando imagens ...')
    plotar_uso_memmoria(df=df, pasta_saida=pasta_saida)
    plotar_tempo_execucao(df=df, pasta_saida=pasta_saida)
    print('Concluído!')

def main():
    print('Iniciando ...')
    args = parser_arguments_plot()
    dicionarios = dicionarios_utilizados()

    tipo_lista = dicionarios['t'][args.t]

    if args.a == 'a':
        pasta = 'buscaLinearV1'
    elif args.a == 'b':
        pasta = 'buscaLinearV2'
    elif args.a == 'c':
        pasta = None
    elif args.a == 'd':
        pasta = None
    elif args.a == 'e':
        pasta = None
    elif args.a == 'f':
        pasta = None

    diretorio_base = getCaminhoOutput(pasta=pasta, algoritmo=args.a)

    for subdiretorio in os.listdir(diretorio_base):
        if subdiretorio.isdigit():
            caminho_arquivo = os.path.join(diretorio_base, subdiretorio, tipo_lista)
            print('Verificando se existe o caminho')

            if os.path.exists(caminho_arquivo):
                print('Caminho encontrado ...')
                for sub_subdir in os.listdir(caminho_arquivo):
                    caminho_completo = os.path.join(caminho_arquivo, sub_subdir)
                    
                    plotar_imagem(caminho_arquivo=caminho_completo)
            else:
                print('Caminho Não Existe: ', caminho_arquivo)
        print('\n')


if __name__ == "__main__":
    main()