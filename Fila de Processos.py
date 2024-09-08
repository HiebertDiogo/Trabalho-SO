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
        # Primeiro processo
        if i == 0: 
            # Considera que o primeiro processo inicia em 0
            if timer == processos[0].tempo_chegada: 
                timer = processos[0].tempo_exec 
                processos[0].tempo_conclusao = timer # Tempo de conclusão e retorno são iguais ao timer, ou o tempo de execução do processo
                processos[0].tempo_retorno = timer
                processos[0].tempo_resposta = 0 # Tempo de resposta e espera é zero para o primeiro processo
                processos[0].tempo_espera = 0
            
            
            # Considera que o primeiro processo não começa em 0 mas sim em outro tempo
            else:
                timer = processos[0].tempo_chegada + processos[0].tempo_exec
                processos[0].tempo_conclusao = timer # Tempo que o processo termina
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

    # Soma de todos os tempos
    for processo in processos:
        tempRetorno += processo.tempo_retorno
        tempRespost += processo.tempo_resposta
        tempEspera += processo.tempo_espera

    # Cálculo das médias dos tempos
    tempRetorno = tempRetorno/numeroProcessos
    tempRespost = tempRespost/numeroProcessos
    tempEspera = tempEspera/numeroProcessos

    return f"FCFS {tempRetorno:.1f} {tempRespost:.1f} {tempEspera:.1f}" #retornamos uma string com os dados do FCFS

############################################################################################################################

def processoSJF(processos):

    numeroProcessos = len(processos)
    timer = 0 # Temporizador
    fila_exec = [] # Fila de executados

    # Termina o processamento até que todos o processos tenham sido executados
    while len(fila_exec) < numeroProcessos:

        fila = [] # Fila dos processos que irão ser executados

        for p in processos:
            # Insere na fila os processos que respeitam o tempo e que não foram executados
            if (p.tempo_chegada <= timer) and (p.executado == False):
                fila.append(p)

        # Organiza a fila de acordo com o tempo de execução
        fila = sorted(fila, key= lambda process: process.tempo_exec)              

        # Reconhece a ociosidade da fila, enquanto não chegam novos processos
        if len(fila) == 0:
            timer += 1
            continue

        # O processo executa apenas uma vez, então diminui-se o tempo atual pelo tempo de chegada do processo
        fila[0].tempo_espera = timer - fila[0].tempo_chegada

        # Cálculo para concluir a execução do processo
        fila[0].tempo_conclusao = timer + fila[0].tempo_exec

        # Diferença entre o tempo atual e o tempo que o processo passou a ser executado
        fila[0].tempo_resposta = timer - fila[0].tempo_chegada

        # Tempo que o processo precisou para ser finalizado
        fila[0].tempo_retorno = fila[0].tempo_conclusao - fila[0].tempo_chegada

        # Atualiza o tempo
        timer += fila[0].tempo_exec

        fila[0].executado = True

        # Adiona a fila de processos finalizados/executados
        fila_exec.append(fila[0])

    tempRetorno = tempRespost = tempEspera = 0

    # Soma de todos os tempos
    for processo in fila_exec:
        tempRetorno += processo.tempo_retorno
        tempRespost += processo.tempo_resposta
        tempEspera += processo.tempo_espera

    # Cálculo das médias dos tempos
    tempRetorno = tempRetorno/numeroProcessos 
    tempRespost = tempRespost/numeroProcessos
    tempEspera = tempEspera/numeroProcessos

    return f"SJF {tempRetorno:.1f} {tempRespost:.1f} {tempEspera:.1f}" #retornamos uma string com os dados do FCFS

############################################################################################################################

def processoRR(processos):

    numeroProcessos = len(processos)
    timer = 0 # Temporizador
    fila_exec = [] # Fila de executados
    fila = [] # Fila dos processos que irão ser executados
    quantum = 2
    aux = None

    # Termina o processamento até que todos o processos tenham sido executados
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

    # Leitura do arquivo txt
    with open('input2.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

        # Foi utilizado o enumerate para enumerar os processo e assim usar o 'j' para formar o nome do processo: P+j, P1- P2 - P3 etc
        for j, linha in enumerate(linhas): 
            dado = linha.split()
            processo = Processo(j+1, int(dado[0]), int(dado[1]))
            processos.append(processo)
    
    # Retorna a lista de processos dos arquivos
    return processos

def main():
    input = readInput()

    # Faz-se uma cópia da lista de processos, para que não haja compartilhamento de endereços com a lista principal
    print(processoFCFS(copy.deepcopy(input)))
    print(processoSJF(copy.deepcopy(input)))
    print(processoRR(copy.deepcopy(input)))

    
# Executa o programa
main()


