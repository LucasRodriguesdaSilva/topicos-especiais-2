import argparse

def arguments_main():
    parser = argparse.ArgumentParser(description='Trabalho Esquenta 2')

    parser.add_argument('--a', required=True, choices=['a','b'], help='Algoritmos para o experimento')
    
    parser.add_argument('--i', required=True, type=int, choices=[1,2,3,4,5,6,7,8,9,10,11,12,13], help='Instâncias a serem utilizadas')
        
    parser.add_argument('--loop', type=int, default=2, help='Quantidade de vezes que o algoritmo sera executado, Padrão 100 iterações')

    return parser.parse_args()


def arguments_plot():
    parser = argparse.ArgumentParser(description='Trabalho Esquenta - Plotagem das Imagens')

    parser.add_argument('--a', required=True, choices=['a','b'], help='Algoritmos para a plotagem dos gráficos')

    return parser.parse_args()

def arguments_medias():
    parser = argparse.ArgumentParser(description='Trabalho Esquenta - Medias')

    parser.add_argument('--a', required=True, choices=['a','b'], help='Algoritmos para a plotagem dos gráficos')

    return parser.parse_args()
    