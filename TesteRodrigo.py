
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

    for i in range(numeroProcessos):#Fazemos a soma de todos os tempos
        tempRetorno += processos[i].tempo_retorno
        tempRespost += processos[i].tempo_resposta
        tempEspera += processos[i].tempo_espera

    tempRetorno = tempRetorno/numeroProcessos #Fazemos a media aqui
    tempRespost = tempRespost/numeroProcessos
    tempEspera = tempEspera/numeroProcessos

    return f"FCFS {tempRetorno:.1f} {tempRespost:.1f} {tempEspera:.1f}" #retornamos uma string com os dados do FCFS

############################################################################################################################

def processoSJF(processos):

    numeroProcessos = len(processos)
    timer = 0 #nosso temporizador
    fila_exec = []
    fila = []

    while len(fila_exec) != numeroProcessos:
        for i in range(numeroProcessos):
            if (processos[i].tempo_chegada <= timer) and (processos[i].executado == False):
                fila.append(processos[i])
                processos[i].executado = True

        nao_executados = [process for process in fila_exec if process.executado == False]

        nao_executados.sort(key = lambda process: process.tempo_exec)

        iter_nao_executados = iter(nao_executados)

        for p in fila:
            if p.executado == True:
                fila_exec.append(p)
            else:
                fila_exec.append(next(iter_nao_executados))  

        # fila_exec = sorted(fila_exec, key= lambda process: process.tempo_exec)
        print(len(fila_exec))
        for i in fila_exec:
            i.teste()

        for i in range(len(fila_exec)):

            if fila_exec[i].executado == True:
                continue
            
            if i == 0: #primeiro processo
                if timer == fila_exec[0].tempo_chegada:#considerando que o primeiro processo inicia em 0
                    timer = fila_exec[0].tempo_exec 
                    fila_exec[0].tempo_conclusao = timer #o tempo de conclusão e retorno são iguais ao timer, ou o tempo de execução do processo
                    fila_exec[0].tempo_retorno = timer
                    fila_exec[0].tempo_resposta = 0 #tempo de resposta e espera é zero para o primeiro processo
                    fila_exec[0].tempo_espera = 0
                else:#agora essa parte considera que o primeiro processo não começa em 0 mas sim em outro tempo
                    timer = fila_exec[0].tempo_chegada + fila_exec[0].tempo_exec
                    fila_exec[0].tempo_conclusao = timer #tempo que o processo termina
                    fila_exec[0].tempo_retorno = fila_exec[0].tempo_conclusao - fila_exec[0].tempo_chegada
                    fila_exec[0].tempo_resposta = 0
                    fila_exec[0].tempo_espera = 0
            else:
                if timer < fila_exec[i].tempo_chegada: #Se não tivemos nenhum processo para executar o timer é incrementado até o tempo que chegue um processo
                    timer = fila_exec[i].tempo_chegada
                fila_exec[i].tempo_resposta = (timer - fila_exec[i].tempo_chegada)
                timer += fila_exec[i].tempo_exec
                fila_exec[i].tempo_conclusao = timer
                fila_exec[i].tempo_retorno = (fila_exec[i].tempo_conclusao - fila_exec[i].tempo_chegada)
                fila_exec[i].tempo_espera = fila_exec[i].tempo_resposta

            fila_exec[i].executado = True

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

    with open('input1.txt', 'r') as arquivo: #lemos os dados do arquivo .txt
        linhas = arquivo.readlines()
        for j, linha in enumerate(linhas): #usamos o enumerate para enumerar os processo e podermos usar o 'j' para formar o nome do processo: P+j, P1- P2 - P3 etc
            dado = linha.split()
            processo = Processo(j+1, int(dado[0]), int(dado[1]))
            processos.append(processo)
           
    return processos

def main():
    input = readInput()
    # print(processoFCFS(input.copy()))
    print(processoSJF(input.copy()))


    # for i in input: #só pra mostras as infos dos processos!
    #     i.show()

main()


