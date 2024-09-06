import copy

class Processo:
    def __init__(self, num, tempo_chegada, tempo_exec):
        self.nome = "P"+ str(num) # aqui seria o campo do nome do processo, ignore por enquanto, mas seria tipo 'P1'
        self.tempo_chegada = tempo_chegada
        self.tempo_exec = tempo_exec
        self.tempo_conclusao = 0
        self.tempo_retorno = 0 
        self.tempo_resposta = 0
        self.tempo_espera = 0
        self.executado = False

    def show(self):#Função pra debug para ver as infos dos processos
        print(f"\nProcesso: {self.nome}")
        print(f"Tempo de Conclusão: {self.tempo_chegada}")
        print(f"Tempo de Conclusão: {self.tempo_exec}")
        print(f"Tempo de Conclusão: {self.tempo_conclusao}")
        print(f"Tempo de Retorno: {self.tempo_retorno}")
        print(f"Tempo de Resposta: {self.tempo_resposta}")
        print(f"Tempo de Espera: {self.tempo_espera}")

    def teste(self):
        print(f"\nProcesso: {self.nome}")


def processoSJF(processos):

    numeroProcessos = len(processos)
    timer = 0 #nosso temporizador
    fila_exec = []
    a = True
    b = 0

    while len(fila_exec) < numeroProcessos:

        fila = []

        for i in range(len(processos)):
            if (processos[i].tempo_chegada <= timer) and (processos[i].executado == False):
                fila.append(processos[i])

        fila = sorted(fila, key= lambda process: process.tempo_exec)              


        if timer < fila[0].tempo_chegada:
            timer = fila[0].tempo_chegada

        fila[0].tempo_conclusao = timer + fila[0].tempo_exec
        fila[0].tempo_retorno = fila[0].tempo_conclusao - fila[0].tempo_chegada
        fila[0].tempo_resposta = timer - fila[0].tempo_chegada
        fila[0].tempo_espera = timer - fila[0].tempo_chegada

        timer += fila[0].tempo_exec


        fila[0].executado = True
        fila_exec.append(fila[0])

    tempRetorno = tempRespost = tempEspera = 0

    for i in range(len(fila_exec)): #Fazemos a soma de todos os tempos
        tempRetorno += fila_exec[i].tempo_retorno
        tempRespost += fila_exec[i].tempo_resposta
        tempEspera += fila_exec[i].tempo_espera

    tempRetorno = tempRetorno/numeroProcessos #Fazemos a media aqui
    tempRespost = tempRespost/numeroProcessos
    tempEspera = tempEspera/numeroProcessos
    

    return f"SJF {tempRetorno:.1f} {tempRespost:.1f} {tempEspera:.1f}" #retornamos uma string com os dados do FCFS


############################################################################################################################

def readInput():
    processos = []

    with open('input3.txt', 'r') as arquivo: #lemos os dados do arquivo .txt
        linhas = arquivo.readlines()
        for j, linha in enumerate(linhas): #usamos o enumerate para enumerar os processo e podermos usar o 'j' para formar o nome do processo: P+j, P1- P2 - P3 etc
            dado = linha.split()
            processo = Processo(j+1, int(dado[0]), int(dado[1]))
            processos.append(processo)
           
    return processos

def main():
    input = readInput()
    # print(processoFCFS(input.copy()))
    print(processoSJF(copy.deepcopy(input)))


    # for i in input: #só pra mostras as infos dos processos!
    #     i.show()


main()