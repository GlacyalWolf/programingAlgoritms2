

def sum(a: list, b: list) -> list:
    matriu=[]
    for i in range(len(a)):
        fila=[]
        for x in range(len(a)):
            fila.append(a[i][x]+b[i][x])
        matriu.append(fila)
    return matriu


