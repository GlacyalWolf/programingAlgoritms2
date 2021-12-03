from easyinput import read
import sys

from easyinput.tokenizer import read_many, read_many_lines

iter=read(int)
playerList=[]
for i in range(iter):
    playerList.append(read_many(str,str))


for i in read_many(str,str):
    
    if i.index("?")==1:
        print(i[0],"has played white against")
    else:
        print(i[1],"has played black against")
    
    for i in playerList:
        
    
    




