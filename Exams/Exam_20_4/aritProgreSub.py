import string
from easyinput import read

length,prog = read(int,int)

num=read(int)
memo=num
cont=1
listOfNum=[]
while num is not None:
    if memo+prog==num:
        cont+=1
        listOfNum.append(memo)
        print(num)
        if cont==length:
            break
    else:
        listOfNum=[]
    num=read(int)
        
print(" ".join(listOfNum))        

    
