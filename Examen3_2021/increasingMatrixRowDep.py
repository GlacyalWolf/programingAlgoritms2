from easyinput import read


def createMatrix(rows, cols) -> list:
    outMatrix = []
    for i in range(rows):
        matrixToInsert = []
        for i in range(cols):
            matrixToInsert.append(read(int))
        outMatrix.append(matrixToInsert)
    return outMatrix


def analyzeRows(matrix: list, row, cols) -> str:
    for i in range(row):

        antNum = matrix[i][0]
        cont = 0
        strNums = (f"{antNum} ")
        for x in range(cols):

            num = matrix[i][x]

            if antNum < num:
                cont += 1
                strNums = strNums+(f"{num} ")

            if cont == cols-1:
                return strNums.rstrip()
            antNum = num
    return "No increasing row found."


row, cols = read(int, int)
print(analyzeRows(createMatrix(row, cols), row, cols))
