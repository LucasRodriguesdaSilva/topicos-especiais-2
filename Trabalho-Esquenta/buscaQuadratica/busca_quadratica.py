def buscarQuadratica(numero_procurado, vet):
    
    contador = 0
    posicao = -1
    entrou = False

    for i in range(len(vet)):
        for j in range(i, len(vet)):
            if vet[i] == numero_procurado:
                if not entrou:
                    posicao = i
                    if vet[j] == numero_procurado:
                        contador += 1
                entrou = True
        
        if contador > 0:
            break

    return posicao