import sys
from easyinput import read

cont=0
for i in range(read(int)):
    line=sys.stdin.readline().rstrip().split()
    memo=int(line[0])
    for i in line:
        if memo>int(i):
            cont+=1
        memo=int(i)
    print(cont)
    cont=0

