import argparse

def parser_arguments():
    parser = argparse.ArgumentParser(description='Trabalho Esquenta - Experimentação de vários algoritmos de busca')

    parser.add_argument('--a', required=True, choices=['a','b','c','d','e','f'], help='Algoritmos para o experimento de acordo com o README.md')
    
    parser.add_argument('--i', required=True, type=int, choices=[1,2,3,4,5,6,7,8,9,10,11,12,13], help='Instâncias a serem utilizadas de acordo com o README.md')
    
    parser.add_argument('--t', required=True, choices=['o','no'], help='Tipo da instância a ser utilizada de acordo com o README.md')
    
    parser.add_argument('--loop', type=int, default=100, help='Quantidade de vezes que o algoritmo sera executado, Padrão 100 iterações')

    return parser.parse_args()
