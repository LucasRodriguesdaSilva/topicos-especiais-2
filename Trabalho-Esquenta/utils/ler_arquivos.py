import os 

class LerArquivos:
    @staticmethod
    def ler_arquivo(caminho_relativo):
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        caminho_arquivo = os.path.join(diretorio_atual, caminho_relativo)

        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()

        return conteudo