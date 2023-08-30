import random

def main(num):
    gerador = random.Random()
    
    
    cont = 0
    numeros = []  # Lista de listas para armazenar os números
    linha = []  # Lista para armazenar os números de cada linha
    for i in range(num):
        
        if(cont < 9):
            numero = gerador.randint(0, num)
            cont = 1 + cont
            linha.append(numero)
        else:
            cont = 0
            numeros.append(linha)
            linha = []
    
    # Salvar a lista de listas em um arquivo de texto
    with open(f'{num}.txt', 'w') as arquivo:
        for linha in numeros:
            linha_formatada = ','.join(map(str, linha))
            arquivo.write(linha_formatada + ' \n')

if __name__ == "__main__":
    lista = [100, 200, 1000, 2000, 5000,10000,50000, 100000,500000,1000000,5000000,10000000,100000000]

    for x in lista:
        print(f'Gerando: {x}.txt ...')
        main(num=x)
        print('Concluído \n')