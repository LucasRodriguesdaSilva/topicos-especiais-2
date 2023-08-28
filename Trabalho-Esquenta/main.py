from buscaLinearV1.busca_linear_v1 import BuscaLinearV1
from utils.arguments_parser import parser_arguments
from utils.ler_arquivos import ler_arquivo
from utils.salvar_dados import salvarInformacoes
from utils.medir_uso_memoria import medirUsoMemoria
from utils.dicionarios_utilizados import dicionarios_utilizados
from utils.output_info import mensagemInicial, imprimirInfo, mensagemConteudo
import cProfile
import os
import psutil
import random
import time
import colorama
from colorama import Fore, Style

def contruirCaminhoInstancia(tipo_lista, nome_instancia):
    nomeInstancia = f'{nome_instancia}.txt'
    caminho_arq = os.path.join('utils', tipo_lista)
    caminho_completo = os.path.join(os.path.dirname(__file__), caminho_arq, nomeInstancia)

    return caminho_completo

def getCaminhoAbsoluto():
    return os.path.dirname(os.path.abspath(__file__))


def medicoes(algoritmo, *args):
    uso_memoria_inicio = medirUsoMemoria()
    indice, tempo_execucao = algoritmo(*args)
    uso_memoria_fim = medirUsoMemoria()

    return indice, tempo_execucao, uso_memoria_inicio, uso_memoria_fim

def criarCaminhoOutput(pasta,tipo_lista, nome_instancia, algoritmo, valor_procurado):
    valor_procurado = str(valor_procurado)
    caminho_relativo = os.path.join(pasta, 'output',algoritmo,nome_instancia,tipo_lista,valor_procurado)
    return caminho_relativo

def main():
    colorama.init()  # Inicializar o colorama
    mensagemInicial()
    caminhoAbsoluto = getCaminhoAbsoluto()
    algoritmo_utilizado = None
    caminho_relativo = None
    conteudo = None
    tipo_lista = None
    nome_instancia = None
    nome_algoritmo = None
    num_loops = 1
    dicionarios = dicionarios_utilizados()

    args = parser_arguments()

    nome_algoritmo = dicionarios['a'][args.a]
    nome_instancia = dicionarios['i'][args.i]
    tipo_lista = dicionarios['t'][args.t]
    num_loops = args.loop

    # if args.x < 0:
    #     valor_procurado = random.randint(0, 99999)
    # else:
    #     valor_procurado = args.x

    if args.loop < 1:
        num_loops = 100
    else:
        num_loops = args.loop

    
    caminho_relativo = contruirCaminhoInstancia(tipo_lista=tipo_lista, nome_instancia=nome_instancia)



    if args.a == 'a':
        algoritmo_utilizado = BuscaLinearV1.busca_linear_v1
        pasta = 'buscaLinearV1'
    elif args.a == 'b':
        algoritmo_utilizado = None
    elif args.a == 'c':
        algoritmo_utilizado = None
    elif args.a == 'd':
        algoritmo_utilizado = None
    elif args.a == 'e':
        algoritmo_utilizado = None
    elif args.a == 'f':
        algoritmo_utilizado = None

    mensagemConteudo()
    conteudo = ler_arquivo(caminho_relativo=caminho_relativo)

    for j in range(3):
        if j == 0:
            valor_procurado = conteudo[0]
        elif j == 1: 
            valor_procurado = conteudo[-1]
        elif j == 2:
            valor_procurado = random.randint(0, 99999)

        imprimirInfo(nome_algoritmo=nome_algoritmo, nome_instancia=nome_instancia, tipo_lista=tipo_lista, num_loops=num_loops, valor_procurado=valor_procurado)

        output = criarCaminhoOutput(pasta=pasta, tipo_lista=tipo_lista, nome_instancia=nome_instancia,algoritmo=args.a, valor_procurado=valor_procurado)

        dicionario_resultados = {}
        for i in range(num_loops):
            print(f"Iteração {i + 1} de {num_loops}", end="\r")  # \r para voltar ao início da linha

        
            resultado, tempo_execucao, uso_memoria_inicio, uso_memoria_fim = medicoes(algoritmo_utilizado,valor_procurado,conteudo)
            diferenca_memoria = uso_memoria_fim - uso_memoria_inicio

            dicionario_resultados[i] = {
                'tempo_execucao': tempo_execucao, 
                'uso_inicial': uso_memoria_inicio, 
                'uso_final': uso_memoria_fim, 
                'uso_diferenca': diferenca_memoria,
                'valor_procurado': valor_procurado,
                'resultado_encontrado': resultado
            }

            time.sleep(0.1)  # Atraso 
            print(" " * len(f"Iteração {i + 1} de {num_loops}"), end="\r")  # Limpar a linha


        print(Fore.GREEN + "Concluído!" + Style.RESET_ALL)  # Imprimir concluído em verde
        salvarInformacoes(dicionario=dicionario_resultados,caminhoAbsoluto=caminhoAbsoluto,pasta=output)
        print('\n')

if __name__ == "__main__":
    main()

