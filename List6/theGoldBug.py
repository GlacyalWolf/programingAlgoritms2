import sys
from easyinput import *


abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
       "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def printDecriptLine(clave, linea):
    transLine = ""

    for i in linea:
        if i != "_":
            for x in range(len(clave)):
                if(clave[x] == i):
                    break

            transLine = transLine+abc[x]

        else:
            transLine = transLine+" "
    print(transLine)


enkriKey = sys.stdin.readline().rstrip()

while enkriKey != "":

    for i in range(read(int)):
        printDecriptLine(enkriKey, sys.stdin.readline().rstrip())

    input()
    enkriKey = sys.stdin.readline().rstrip()
