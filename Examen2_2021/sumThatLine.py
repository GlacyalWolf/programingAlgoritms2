from easyinput import *
import sys


def sumalinea(line):
    suma = 0
    for i in line:
        suma += int(i)
    return suma


counter3 = 0

line = sys.stdin.readline().rstrip().split()

while line != []:

    for i in line:
        if int(i) % 10 == 3:
            counter3 += 1
    if counter3 % 2 == 0 and counter3 != 0:
        print(sumalinea(line))
        break
    else:
        counter3 = 8

    line = sys.stdin.readline().rstrip().split()
if(line == []):
    print(-1)
