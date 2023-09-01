def buscaCubica(numero_procurado, vet):
    posicao = -1

    for i in range(len(vet)):
        for j in range(len(vet)):
            for l in range(len(vet)):
                if vet[i] == numero_procurado and vet[j] == numero_procurado and vet[l] == numero_procurado:
                    posicao = i

    return posicao
