import time
class BuscaLinearV1:
    @staticmethod
    def busca_linear_v1(x, v):
        inicio = time.time()
        indice = -1
        for i in range(len(v)):
            if v[i] == x:
                indice = i
        
        fim = time.time()
        tempo_execucao = fim - inicio

        return indice, tempo_execucao
