def busca_ternaria(x,vet):
    n = len(vet)
    inicio = 0
    fim = n - 1

    while inicio <= fim:
        meio_esquerdo = inicio + (fim - inicio) // 3
        meio_direito = fim - (fim - inicio) // 3

        if vet[meio_esquerdo] == x:
            return meio_esquerdo
        elif vet[meio_direito] == x:
            return meio_direito
        elif vet[meio_esquerdo] > x:
            fim = meio_esquerdo - 1
        elif vet[meio_direito] < x:
            inicio = meio_direito + 1
        else:
            inicio = meio_esquerdo + 1
            fim = meio_direito - 1

    return -1
