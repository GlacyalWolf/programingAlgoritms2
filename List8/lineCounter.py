from sys import stdin
from easyinput import *

wordToSeek=read(str)

cont=0
for line in stdin:
    line=input().rstrip('\n').split()
    if wordToSeek in line:
        cont+=1    
print(cont)

