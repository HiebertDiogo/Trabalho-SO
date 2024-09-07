import copy

class Processo:
    def __init__(self, num, tempo_chegada, tempo_exec):
        self.nome = "P"+ str(num) # aqui seria o campo do nome do processo, ignore por enquanto, mas seria tipo 'P1'
        self.tempo_chegada = tempo_chegada
        self.tempo_exec = tempo_exec
        self.tempo_conclusao = 0
        self.tempo_retorno = 0 
        self.tempo_resposta = None
        self.tempo_espera = 0
        self.executado = False

    def show(self):#Função pra debug para ver as infos dos processos
        print(f"\nProcesso: {self.nome}")
        print(f"Tempo de Chegada: {self.tempo_chegada}")
        print(f"Tempo de Execução: {self.tempo_exec}")
        print(f"Tempo de Conclusão: {self.tempo_conclusao}")
        print(f"Tempo de Retorno: {self.tempo_retorno}")
        print(f"Tempo de Resposta: {self.tempo_resposta}")
        print(f"Tempo de Espera: {self.tempo_espera}")

############################################################################################################################

def processoFCFS(processos):

    numeroProcessos = len(processos)
    timer = 0 #nosso temporizador

    for i in range(numeroProcessos):
        if i == 0: #primeiro processo
            if timer == processos[0].tempo_chegada:#considerando que o primeiro processo inicia em 0
                timer = processos[0].tempo_exec 
                processos[0].tempo_conclusao = timer #o tempo de conclusão e retorno são iguais ao timer, ou o tempo de execução do processo
                processos[0].tempo_retorno = timer
                processos[0].tempo_resposta = 0 #tempo de resposta e espera é zero para o primeiro processo
                processos[0].tempo_espera = 0
            else:#agora essa parte considera que o primeiro processo não começa em 0 mas sim em outro tempo
                timer = processos[0].tempo_chegada + processos[0].tempo_exec
                processos[0].tempo_conclusao = timer #tempo que o processo termina
                processos[0].tempo_retorno = processos[0].tempo_conclusao - processos[0].tempo_chegada
                processos[0].tempo_resposta = 0
                processos[0].tempo_espera = 0

        else:
            if timer < processos[i].tempo_chegada: #Se não tivemos nenhum processo para executar o timer é incrementado até o tempo que chegue um processo
                timer = processos[i].tempo_chegada
            processos[i].tempo_resposta = (timer - processos[i].tempo_chegada)
            timer += processos[i].tempo_exec
            processos[i].tempo_conclusao = timer
            processos[i].tempo_retorno = (processos[i].tempo_conclusao - processos[i].tempo_chegada)
            processos[i].tempo_espera = processos[i].tempo_resposta

        processos[i].executado = True
            
    tempRetorno = tempRespost = tempEspera = 0

    for processo in processos: #Fazemos a soma de todos os tempos
        tempRetorno += processo.tempo_retorno
        tempRespost += processo.tempo_resposta
        tempEspera += processo.tempo_espera

    tempRetorno = tempRetorno/numeroProcessos #Fazemos a media aqui
    tempRespost = tempRespost/numeroProcessos
    tempEspera = tempEspera/numeroProcessos

    return f"FCFS {tempRetorno:.1f} {tempRespost:.1f} {tempEspera:.1f}" #retornamos uma string com os dados do FCFS

############################################################################################################################

def processoSJF(processos):

    numeroProcessos = len(processos)
    timer = 0 #nosso temporizador
    fila_exec = []

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

    for processo in fila_exec: #Fazemos a soma de todos os tempos
        tempRetorno += processo.tempo_retorno
        tempRespost += processo.tempo_resposta
        tempEspera += processo.tempo_espera

    tempRetorno = tempRetorno/numeroProcessos #Fazemos a media aqui
    tempRespost = tempRespost/numeroProcessos
    tempEspera = tempEspera/numeroProcessos
    

    return f"SJF {tempRetorno:.1f} {tempRespost:.1f} {tempEspera:.1f}" #retornamos uma string com os dados do FCFS

############################################################################################################################

def processoRR(processos):

    return
    # return f"RR {tempRetorno:.1f} {tempRespost:.1f} {tempEspera:.1f}" #retornamos uma string com os dados do FCFS

############################################################################################################################

def readInput():
    processos = []

    with open('input1.txt', 'r') as arquivo: #lemos os dados do arquivo .txt
        linhas = arquivo.readlines()
        for j, linha in enumerate(linhas): #usamos o enumerate para enumerar os processo e podermos usar o 'j' para formar o nome do processo: P+j, P1- P2 - P3 etc
            dado = linha.split()
            processo = Processo(j+1, int(dado[0]), int(dado[1]))
            processos.append(processo)
           
    return processos

def main():
    input = readInput()
    print(processoFCFS(copy.deepcopy(input)))
    print(processoSJF(copy.deepcopy(input)))
    print(processoRR(copy.deepcopy(input)))

    # for i in input: #só pra mostras as infos dos processos!
    #     i.show()

main()


