import copy

def FIFO(num_quadros, ref):
    # Inicialização das variáveis
    quadros = [None for _ in range(num_quadros)] # Preenchimento dos quadros com o tamanho fornecido
    contador = pos = 0                           # Contador de Substituição, Posição Corrente

    # Enquanto houver páginas na sequência de referências
    while len(ref) != 0:
        pag = ref[0]  # Página da vez

        # Não encontrando a página nos quadros
        if pag not in quadros:
            quadros[pos] = pag             # Substitui-se pela posição atual
            pos = (pos + 1) % num_quadros  # Atualiza a posição
            contador += 1                  # Incrementa-se o contador de quadros

        ref.pop(0)                         # Remove a página atual da sequência de referências

    return f"FIFO {contador}"

def OTM(num_quadros, ref):
    # Inicialização das variáveis
    quadros = []  # Cria-se os quadros com a paginação vazia
    contador = 0  # Contador de Substituição

    # Preenche-se os quadros com as primeiras páginas
    while(contador < num_quadros and len(ref) > 0):
        if ref[0] not in quadros:
            quadros.append(ref[0])
            ref.pop(0)
            contador += 1
        else:
            ref.pop(0)

    # Enquanto houver páginas na sequência de referências
    while len(ref) != 0:
        p = ref[0] # Página da vez
        
        # Se a página já está na fila, apenas remove da referência
        if p in quadros:
            ref.pop(0)
        else:
            # Caso a página não esteja na fila, ocorre uma substituição
            indiceMaisLonge = -1
            numeroMaisLonge = -1
            
            # Identifica qual página na quadros será usada mais tarde (ou não será usada)
            for pagina in quadros:
                if pagina in ref:
                    dist = ref.index(pagina)
                else:
                    dist = float('inf')     # Se a página não está mais em uso, ela pode ser substituída

                if dist > indiceMaisLonge:
                    indiceMaisLonge = dist
                    numeroMaisLonge = pagina

            # Remove a página que será usada mais longe ou não será mais usada
            quadros.remove(numeroMaisLonge)
            quadros.append(p)               # Adiciona a nova página
            ref.pop(0)                      # Remove a página atual da sequência de referências
            contador += 1

    return f"OTM {contador}"

def LRU(num_quadros, ref):
    # Inicialização das variáveis
    quadros = [None for _ in range(num_quadros)]                # Lista que armazena as páginas
    quadros_count = [float('inf') for _ in range(num_quadros)]  # Lista que armazena a distância de cada página
    contador = 0 

    # Enquanto houver páginas na sequência de referências
    while len(ref) != 0:
        pag = ref[0] # Página da vez

        # Se a página não estiver nos quadros
        if pag not in quadros:
            pos_in_quadros = quadros_count.index(max(quadros_count)) # Obtem-se o índice da maior distância
            quadros[pos_in_quadros] = pag                            # Atualiza-se a página em quadros
            quadros_count[pos_in_quadros] = 0                        # Atualiza-se a distância da nova página
            contador += 1                                            # Contabiliza-se uma substituição 

        # Se a página estiver nos quadros
        if pag in quadros:
            pos_in_quadrosCount = quadros.index(pag)                 # Obtem-se o índice da página
            quadros_count[pos_in_quadrosCount] = 0                   # Atualiza-se a distância da página

        # Incrementa o valor de todas as distâncias de páginas
        for i in range(num_quadros):
            quadros_count[i] += 1


        ref.pop(0) # Remove a página atual da sequência de referências

    return f"LRU {contador}"


def readInput(file_name):
    referencias = []

    with open(file_name, "r") as file:
        lines = file.readlines()

        num_quadros = int(lines[0])

        for line in lines[1:]:
            referencias.append(int(line))

    return num_quadros, referencias

def main():
    # for i in range(1,8):
    #     input_numQuadros, input_seq = readInput(f"Projeto 2/input{i}.txt")
        
    #     print(FIFO(input_numQuadros, copy.deepcopy(input_seq)))
    #     print(OTM(input_numQuadros, copy.deepcopy(input_seq)))
    #     print(LRU(input_numQuadros, copy.deepcopy(input_seq)))
    #     print()

    input_numQuadros, input_seq = readInput(f"Projeto 2/input7.txt")
        
    print(FIFO(input_numQuadros, copy.deepcopy(input_seq)))
    print(OTM(input_numQuadros, copy.deepcopy(input_seq)))
    print(LRU(input_numQuadros, copy.deepcopy(input_seq)))
    
main()
