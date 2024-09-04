
class Processo:
    def __init__(self, num,tempo_chegada, tempo_exec):
        self.nome = "P"+ str(num) # aqui seria o campo do nome do processo, ignore por enquanto, mas seria tipo 'P1'
        self.tempo_chegada = tempo_chegada
        self.tempo_exec = tempo_exec
        self.tempo_conclusao = 0
        self.tempo_retorno = 0 
        self.tempo_resposta = 0
        self.tempo_espera = 0

    def show(self):#Função pra debug para ver as infos dos processos
        print(f"Tempo de Conclusão: {self.tempo_conclusao}")
        print(f"Tempo de Retorno: {self.tempo_retorno}")
        print(f"Tempo de Resposta: {self.tempo_resposta}")
        print(f"Tempo de Espera: {self.tempo_espera}")

def processoFCFS(input):

    numeroProcessos = len(input)
    timer = 0 #nosso temporizador
    tempRetorno = 0
    tempRespost = 0
    tempEspera = 0

    for i in range(numeroProcessos):
        if i == 0: #primeiro processo
            if timer == input[0].tempo_chegada:#considerando que o primeiro processo inicia em 0
                timer = input[0].tempo_exec 
                input[0].tempo_conclusao = timer #o tempo de conclusão e retorno são iguais ao timer, ou o tempo de execução do processo
                input[0].tempo_retorno = timer
                input[0].tempo_resposta = 0 #tempo de resposta e espera é zero para o primeiro processo
                input[0].tempo_espera = 0
            else:#agora essa parte considera que o primeiro processo não começa em 0 mas sim em outro tempo
                timer = input[0].tempo_chegada + input[0].tempo_exec
                input[0].tempo_conclusao = timer #tempo que o processo termina
                input[0].tempo_retorno = input[0].tempo_conclusao - input[0].tempo_chegada
                input[0].tempo_resposta = 0
                input[0].tempo_espera = 0
        else:
            if timer < input[i].tempo_chegada: #Se não tivemos nenhum processo para executar o timer é incrementado até o tempo que chegue um processo
                timer = input[i].tempo_chegada
            input[i].tempo_resposta = (timer - input[i].tempo_chegada)
            timer += input[i].tempo_exec
            input[i].tempo_conclusao = timer
            input[i].tempo_retorno = (input[i].tempo_conclusao - input[i].tempo_chegada)
            input[i].tempo_espera = input[i].tempo_resposta
            

    for i in range(numeroProcessos):#Fazemos a soma de todos os tempos
        tempRetorno += input[i].tempo_retorno
        tempRespost += input[i].tempo_resposta
        tempEspera += input[i].tempo_espera

    tempRetorno = tempRetorno/numeroProcessos #Fazemos a media aqui
    tempRespost = tempRespost/numeroProcessos
    tempEspera = tempEspera/numeroProcessos

    return f"FCFS {tempRetorno:.1f} {tempRespost:.1f} {tempEspera:.1f}" #retornamos uma string com os dados do FCFS

def readInput():
    processos = []

    with open('input.txt', 'r') as arquivo: #lemos os dados do arquivo .txt
        linhas = arquivo.readlines()
        for j, linha in enumerate(linhas): #usamos o enumerate para enumerar os processo e podermos usar o 'j' para formar o nome do processo: P+j, P1- P2 - P3 etc
            dado = linha.split()
            processo = Processo(j+1, int(dado[0]), int(dado[1]))
            processos.append(processo)
           
    return processos

def main():
    input = readInput()
    print(processoFCFS(input))

    for i in input: #só pra mostras as infos dos processos!
        i.show()
        print("\n")

main()


