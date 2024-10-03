import copy

def FIFO(quadros, ref):
    fila = [None for _ in range(quadros)]
    contador = pos = 0

    while(len(ref) != 0):
        for p in ref[:quadros]:
            if p not in fila:
                fila[pos] = p
                pos = (pos + 1) % quadros
                contador += 1

            ref.pop(0)

    return f"FIFO {contador}"

def OTM(quadros, ref):
    fila = []  # vamos criar a fila da paginação vazia no começo
    contador = 0  # contagem de substituições

    # Preenche a fila com as primeiras páginas até encher o número de quadros disponíveis
    for i in range(quadros):
        fila.append(ref[0])
        ref.pop(0)
        contador += 1

    # Enquanto houver páginas na sequência de referências
    while len(ref) != 0:
        p = ref[0]
        
        # Se a página já está na fila, apenas remove da referência
        if p in fila:
            ref.pop(0)
        else:
            # Caso a página não esteja na fila, ocorre uma substituição
            indiceMaisLonge = -1
            numeroMaisLonge = -1
            
            # Identifica qual página na fila será usada mais tarde (ou não será usada)
            for pagina in fila:
                if pagina in ref:
                    dist = ref.index(pagina)
                else:
                    dist = float('inf')  # Se a página não está mais em uso, ela pode ser substituída

                if dist > indiceMaisLonge:
                    indiceMaisLonge = dist
                    numeroMaisLonge = pagina

            # Remove a página que será usada mais longe ou não será mais usada
            fila.remove(numeroMaisLonge)
            fila.append(p)  # Adiciona a nova página
            ref.pop(0)  # Remove da sequência de referências
            contador += 1

    return f"OTM: {contador}"

def LRU(quadros, ref):
    fila = [None for _ in range(quadros)]
    contador = 0

    while(len(ref) != 0):
        for p in range():
            1

def readInput(file_name):
    referencias = []

    with open(file_name, "r") as file:
        lines = file.readlines()

        quadros = int(lines[0])

        for line in lines[1:]:
            referencias.append(int(line))

    return quadros, referencias

def main():
    for i in range(1,5):
        input_quadros, input_seq = readInput(f"Projeto 2/input{i}.txt")
        
        print(FIFO(input_quadros, copy.deepcopy(input_seq)))
        print(OTM(input_quadros, copy.deepcopy(input_seq)))
        print(LRU(input_quadros, copy.deepcopy(input_seq)))

main()