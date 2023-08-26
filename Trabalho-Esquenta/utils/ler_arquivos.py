import os 

def ler_arquivo(caminho_relativo):
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, caminho_relativo)

    with open(caminho_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    
    linhas = conteudo.split('\n')
    vetor = []

    for linha in linhas:
        numeros = linha.split(',')
        for numero_str in numeros:
            if numero_str.strip():
                numero = int(numero_str)
                vetor.append(numero)
    
    return vetor