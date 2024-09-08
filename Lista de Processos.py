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
        self.tempo_chegada_aux = tempo_chegada

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


def processoRR(processos):

    numeroProcessos = len(processos)
    timer = 0 # Temporizador
    fila_exec = [] # Fila de executados
    fila = [] # Fila dos processos que irão ser executados
    quantum = 2
    aux = None

    while len(fila_exec) < numeroProcessos:

        for p in processos:
            # Preenche a fila com os inputs, respeitando o tempo, a não duplicidade e flag de executado
            if (p.executado == False) and (p not in fila) and (p.tempo_chegada <= timer) and (p != aux):
                fila.append(p)
        # Adiciona o último processo que foi executado ao final da fila
        if aux is not None and aux.tempo_exec != 0:
            fila.append(aux)
        
        # Reconhece a ociosidade da fila, enquanto não chegam novos processos
        if len(fila) == 0:
            timer += 1
            continue

        # Diminui o tempo de chegada do processo atual, com seu antigo tempo de conclusão.
        # Quando o tempo de conclusão é igual a 0, significa que é a primeira vez do processo na fila, por isso diminui-se pelo tempo de chegada
        fila[0].tempo_espera += (timer - fila[0].tempo_conclusao) if (fila[0].tempo_conclusao > 0) else (timer - fila[0].tempo_chegada)

        # Calcula o tempo de conclusão da etapa atual de acordo com o tamanho do quantum
        fila[0].tempo_conclusao = (timer + quantum) if (fila[0].tempo_exec > quantum) else (timer + fila[0].tempo_exec)

        # Calcula apenas uma vez e repete o valor, diminui o timer atual pelo tempo de chegada do processo
        fila[0].tempo_resposta = (timer - fila[0].tempo_chegada) if (fila[0].tempo_resposta is None) else fila[0].tempo_resposta
        
        # Atualiza o timer de acordo com o quantum, ou com o que restou do tempo de execução do processo
        timer += quantum if (fila[0].tempo_exec > quantum) else fila[0].tempo_exec

        # Decrementa o tempo restante para a execução do processo
        fila[0].tempo_exec -= quantum if (fila[0].tempo_exec > quantum) else fila[0].tempo_exec
        
        # Verifica se o processo chegou a um fim de execução
        if fila[0].tempo_exec == 0:
            # Diminui o tempo atual de finalização do processo com o tempo de chegada
            fila[0].tempo_retorno = timer - fila[0].tempo_chegada
            # Faz o set da flag, indicando que o processo foi completamente executado
            fila[0].executado = True
            # Adiciona a fila dos processos executados
            fila_exec.append(fila[0])

        # Remove o processo que acabou de ser executado, para assim coloca-lo no final da fila
        aux = fila.pop(0)  # Atualizando 'aux' com o processo atual

    tempRetorno = tempRespost = tempEspera = 0

    for processo in fila_exec: #Fazemos a soma de todos os tempos
        tempRetorno += processo.tempo_retorno
        tempRespost += processo.tempo_resposta
        tempEspera += processo.tempo_espera

    tempRetorno = tempRetorno/numeroProcessos #Fazemos a media aqui
    tempRespost = tempRespost/numeroProcessos
    tempEspera = tempEspera/numeroProcessos
    

    return f"RR {tempRetorno:.1f} {tempRespost:.1f} {tempEspera:.1f}" #retornamos uma string com os dados do RR


############################################################################################################################

def readInput():
    processos = []

    with open('input2.txt', 'r') as arquivo: #lemos os dados do arquivo .txt
        linhas = arquivo.readlines()
        for j, linha in enumerate(linhas): #usamos o enumerate para enumerar os processo e podermos usar o 'j' para formar o nome do processo: P+j, P1- P2 - P3 etc
            dado = linha.split()
            processo = Processo(j+1, int(dado[0]), int(dado[1]))
            processos.append(processo)
           
    return processos

def main():
    input = readInput()
    # print(processoFCFS(copy.deepcopy(input)))
    # print(processoSJF(copy.deepcopy(input)))
    print(processoRR(copy.deepcopy(input)))




    # for i in input: #só pra mostras as infos dos processos!
    #     i.show()


main()
