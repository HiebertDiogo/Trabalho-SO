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
    fila = [None for _ in range(quadros)]
    contador = 0

    while(len(ref) != 0):
        1
        
    return

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