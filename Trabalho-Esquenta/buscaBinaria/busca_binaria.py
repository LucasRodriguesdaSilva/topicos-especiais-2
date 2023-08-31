import time

def pesquisa_binaria(x, v, e, d):
    meio = (e + d) // 2
    if v[meio] == x:
        return meio
    if e >= d:
        return -1
    elif v[meio] < x:
        return pesquisa_binaria(x, v, meio + 1, d)
    else:
        return pesquisa_binaria(x, v, e, meio - 1)
