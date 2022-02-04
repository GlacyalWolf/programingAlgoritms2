from xmlrpc.client import Boolean
from easyinput import *
import sys

def createListZero(size) -> list:
    zeroList=[]
    for i in range(size):
        zeroList.append(0)
    return zeroList

def readMatrix(size) -> list:
    magicSquare=[]
    

    for i in range(size):
        magicSquareRow=[]
        for i in range(size):
            magicSquareRow.append(read(int))
        magicSquare.append(magicSquareRow)


    return magicSquare

def isMagic(m:list) -> bool:
    size=len(m)
    zerolist=createListZero(size*size)
    for x in range(size):
        for y in range(size):            
            ##Repetit?
            if(1<=m[x][y]<=size**2):
                if(zerolist[m[x][y]]==0):
                    zerolist[m[x][y]]=1
                else:
                    return False
            else:
                return False
    ##rows
    srow=sum(m[0])
    for i in range(1,size):
        if(srow!=sum(m[i])):
            return False
    
    ##colums
    scol=[]
    for i in range(len(size)):
        scol.append(m[i][0])
    scol=sum(scol)
    for x in range(1,len(size)):
        col=0
        for y in range(len(size)):
            col+=m[y][x]
        if(scol!=col):
            return False
    
    ##diagonals
    sdig=0
    sdig2=0
    for i in range(size):
        sdig+=m[i][i]
        sdig2+=m[i][size-i]
    if sdig2!=sdig:
        return False

    
    return True        
        
if(isMagic(read(int))):
    print("yes")
else:
    print("no")

