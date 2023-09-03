import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def main():
    pasta = 'mediaMemoria'
    tipo = 'O'
    df = pd.read_csv(f'{pasta}/medias{tipo}.csv')
    novos_nomes = {coluna: str(i) for i, coluna in enumerate(df.columns[1:], start=1)}
    df = df.rename(columns=novos_nomes)
    # Itere pelas linhas do DataFrame e crie um gráfico para cada linha
    for index, row in df.iterrows():
        # Obtenha os valores das colunas 2 em diante
        valores = row[1:]
    
        # Crie um gráfico de linha para os valores
        plt.plot(valores, label=row['Algoritmos'])

        # Adicione rótulos aos eixos e uma legenda
        plt.xlabel('Instâncias')
        plt.ylabel('Valores')
        plt.legend()

        nome_arquivo = f"{pasta}/{row['Algoritmos']}_{tipo}.png"
        plt.savefig(nome_arquivo)

        # Feche a figura atual para liberar recursos
        plt.close()


# Função para criar histogramas
def criar_histograma(df, instancia_nome):
    colunas_de_dados = df.columns[1:]  # Obtém as colunas de dados (excluindo a coluna "Algoritmos")
    
    # Itera pelas colunas de dados e cria um histograma para cada uma
    for coluna in colunas_de_dados:
        plt.figure()  # Cria uma nova figura
        plt.hist(df[coluna], bins=10, color='blue', alpha=0.7)  # Cria o histograma
        
        # Personaliza o título do gráfico com o nome da coluna e da instância
        plt.title(f'Histograma para {coluna} - {instancia_nome}')
        
        # Rótulos dos eixos x e y (ajuste conforme necessário)
        plt.xlabel('Valores')
        plt.ylabel('Contagem')


def hist():
    df1 = pd.read_csv('mediaMemoria/mediasNO.csv')
    df2 = pd.read_csv('mediaMemoria/mediasO.csv')

    # Obtém os nomes dos algoritmos
    algoritmos = df1['Algoritmos']

    # Calcula as médias dos valores para cada arquivo
    media_arquivo1 = df1.iloc[:, 1:].mean(axis=1)
    media_arquivo2 = df2.iloc[:, 1:].mean(axis=1)

    # Configuração para a criação do gráfico
    largura_barra = 0.35
    indice = np.arange(len(algoritmos))

    # Crie o gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))

    bar1 = ax.bar(indice - largura_barra/2, media_arquivo1, largura_barra, label='Não Ordernados', color='blue')
    bar2 = ax.bar(indice + largura_barra/2, media_arquivo2, largura_barra, label='Ordenados', color='purple')

    # Personalize o gráfico
    ax.set_xlabel('Algoritmos')
    ax.set_ylabel('Média de Consumo de Memória (MB)')
    #ax.set_title('Média dos Valores por Algoritmo e Tempo de Execução (s)')
    ax.set_xticks(indice)
    ax.set_xticklabels(algoritmos, rotation=45, ha='right')
    ax.legend()

    plt.tight_layout()
    plt.savefig('memoria_mediaGeral.png')

if __name__ == "__main__":
    #main()
    hist()