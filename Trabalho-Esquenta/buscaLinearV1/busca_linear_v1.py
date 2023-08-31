import time
class BuscaLinearV1:
    @staticmethod
    def busca_linear_v1(x, v):
        indice = -1
        for i in range(len(v)):
            if v[i] == x:
                indice = i
                
        return indice
