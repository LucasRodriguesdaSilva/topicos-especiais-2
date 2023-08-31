import time
class BuscaLinearV2:
    @staticmethod
    def busca_linear_v2(x, v):
        inicio = time.time()
        for i in range(len(v)):
            if v[i] == x:
                fim = time.time()
                tempo_execucao = fim - inicio
                return i, tempo_execucao

        fim = time.time()
        tempo_execucao = fim - inicio
        return -1, tempo_execucao
