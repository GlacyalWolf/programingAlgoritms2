from easyinput import *
import sys


c=[0,0,0,0,0,0,0,0,0,0,0,0]
line=sys.stdin.readline().split()

##while line is not None:
    
for i in line:
    c[int(i)-1]+=1


for i in range(1,12):
    if c[i] !=0:
        print(f"{i+1} : {c[i]}")

