from utils.dicionarios_utilizados import dicionarios_utilizados
from utils.salvar_dados import salvarInformacoes
from utils.ler_arquivos import ler_arquivo
from maxVal1.max_val_1 import maxVal1
from maxVal2.max_val_2 import maxVal2
import utils.arguments as arguments
import utils.output_info as infos
import os 
import tracemalloc
import time 
import colorama
from colorama import Fore, Style

def contruirCaminhoInstancia(tipo_lista, nome_instancia):
    nomeInstancia = f'{nome_instancia}.txt'
    caminho_arq = os.path.join('utils', tipo_lista)
    caminhoAbsoluto = getCaminhoAbsoluto()
    caminho_completo = os.path.join(caminhoAbsoluto, caminho_arq, nomeInstancia)

    return caminho_completo

def getCaminhoAbsoluto():
    return os.path.dirname(os.path.abspath(__file__))

def criarCaminhoOutput(pasta, nome_instancia):
    caminho_relativo = os.path.join(pasta, 'output',nome_instancia)
    return caminho_relativo

def medicoes(algoritmo, *args):
    # uso_memoria_inicio = medirUsoMemoria()
    tracemalloc.start()
    #Inicio do tempo
    inicio = time.time()
    #Executa o algoritmo
    maximo = algoritmo(*args)
    #Termina a contagem do tempo
    fim = time.time()
    tempo_execucao = fim - inicio
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    # uso_memoria_fim = medirUsoMemoria()
    current = current / 10**6
    peak = peak / 10**6

    return tempo_execucao, current, peak

def main():
    colorama.init()
    infos.mensagemInicial()
    caminhoAbsoluto = getCaminhoAbsoluto()
    algoritmo = None
    dicionarios = dicionarios_utilizados()

    args = arguments.arguments_main()

    nome_algoritmo = dicionarios['a'][args.a]
    nome_instancia = dicionarios['i'][args.i]
    tipo_lista = dicionarios['t']['no']

    num_loops = args.loop

    if args.loop < 1:
        num_loops = 100
    else:
        num_loops = args.loop


    caminho_relativo = contruirCaminhoInstancia(tipo_lista=tipo_lista, nome_instancia=nome_instancia)

    if args.a == 'a':
        algoritmo = maxVal1
        pasta = 'maxVal1'
    else:
        algoritmo = maxVal2
        pasta = 'maxVal2'


    infos.mensagemConteudo()
    conteudo = ler_arquivo(caminho_relativo=caminho_relativo)
    print('Instância na memória!')

    infos.imprimirInfoPadrao(nome_algoritmo=nome_algoritmo, nome_instancia=nome_instancia, tipo_lista=tipo_lista, num_loops=num_loops)

    output = criarCaminhoOutput(pasta=pasta, nome_instancia=nome_instancia)

    resultados = {}
    for i in range(num_loops):
        print(f"Iteração {i + 1} de {num_loops}", end="\r")  # \r para voltar ao início da linha

        n = len(conteudo)
        if args.a == 'a':
            tempo_execucao, uso_memoria_atual, uso_memoria_pico = medicoes(algoritmo,conteudo,n)
        else:
            init = 0
            end = n - 1
            tempo_execucao, uso_memoria_atual, uso_memoria_pico = medicoes(algoritmo,conteudo,init, end)


        resultados[i] = {}  # Inicialize um dicionário vazio para esta iteração

        # Adicione os dados relevantes a este dicionário de iteração
        resultados[i]["Tempo de Execucao (s)"] = tempo_execucao
        resultados[i]["Uso de Memoria - atual (MB)"] = uso_memoria_atual
        resultados[i]["Uso de Memoria - Pico (MB)"] = uso_memoria_pico

        time.sleep(0.1)  # Atraso 
        print(" " * len(f"Iteração {i + 1} de {num_loops}"), end="\r")  # Limpar a linha


    salvarInformacoes(dados=resultados,caminhoAbsoluto=caminhoAbsoluto,pasta=output)

    print(Fore.GREEN + "Concluído!" + Style.RESET_ALL)  # Imprimir concluído em verde

    


if __name__ == "__main__":
    main()