import time
class BuscaLinearV2:
    @staticmethod
    def busca_linear_v2(x, v):
        for i in range(len(v)):
            if v[i] == x:
                return i
                
        return -1
