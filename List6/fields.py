from easyinput import read
from numpy import append


filas,col=read(int,int)
rectangles=0

def readMatrix(row,col):
    matrix=[]
    for i in range(row):
        addrow= []
        for i in range(col):
            addrow.append(read(int))
        matrix.append(addrow)
        addrow=[]
    return matrix

field=readMatrix(filas,col)
fieldsCount=0

for i in range(filas):
    for x in range(col):
        if field[i][x]!=0:
            if x==col-1 and field[i][x+1]==0:
                fieldsCount+=1
            if i==filas-1 and field[i+1][x]==0:
                fieldsCount+=1

            elif x!=col-1 and i==filas-1 and field[i+1][x]==0 and field[i][x+1]==0:
                fieldsCount+=1
            print (fieldsCount)    
print(fieldsCount)


