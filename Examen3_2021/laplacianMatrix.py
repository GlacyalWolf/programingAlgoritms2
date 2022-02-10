from easyinput import read


def createMatrix(n) -> list:
    outMatrix = []
    for i in range(n):
        matrixToInsert = []
        for i in range(n):
            matrixToInsert.append(read(int))
        outMatrix.append(matrixToInsert)
    return outMatrix


n = read(int)
diagonalMatrix = createMatrix(n)

for i in range(n):
    diagonalMatrix[i][i] = sum(diagonalMatrix[i])
    for x in range(n):
        if diagonalMatrix[i][x] == 1 and x != i:
            diagonalMatrix[i][x] = -1

string = ""
for i in diagonalMatrix:
    for x in i:
        string = string+(f"{x} ")
    string = string.rstrip()+"\n"

print(string)
