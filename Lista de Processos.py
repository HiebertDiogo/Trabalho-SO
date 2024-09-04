# Programa SO - Lista de Processos
from queue import Queue

"""
- Leitura dos inputs e ordenação segundo o tempo de chegada
- Contador responsável pela posição temporal da fila
- Lista que armazena o Tempo de Retorno, Resposta, Espera de cada processo. Inicio para cada processo: [[0,...],[0,...],[0,...]]
    - [ [0,0,0], [0,0,0], [0,0,0], [0,0,0] ] 
"""


# def returnTime():

# def answerTime():

# def waitTime():


def processoFCFS(input):
    dados_processos = [list([[0],[0],[0]]) for i in range(len(input))]
    # dados_processos[][0] = Registro do tempo de Retorno
    # dados_processos[][1] = Registro do tempo de Resposta
    # dados_processos[][2] = Registro do tempo de Espera

    apontador = 0
    final_time = sum(i[1] for i in input) # Corrigir

    while apontador <= final_time:
        i = 0
        dados_processos[i][0][0] = input[0][1] - apontador
        dados_processos[i][1][0] = input[0][0] - apontador
        dados_processos[i][2][0] = apontador - input[0][0]

        apontador += input[i][1]
        i += 1

    return dados_processos





# def processoSJF(input):


# def processoRR(input):
#     input = sorted(input)
#     return input


def readInput():
    processos = []
    a= 0

    while a < 4: # EOF
        processo = input().split()
        processo = [int(i) for i in processo]
        processos.append(processo)
        a += 1

    # Ordena o input de acordo com o tempo de chegada
    processos.sort(key=lambda x: x[0])

    return processos

def main():
    input = readInput()
    # print(input)

    # print(processoFCFS(input))

    apontador = 0


main()


