import sys

BI = "beginning"
EN = "end"

lista = sys.stdin.readline().lower().split()

if BI in lista and EN in lista and lista.index(EN) > lista.index(BI):
    print((lista.index(EN)-lista.index(BI))-1)

else:
    print("Wrong sequence")
