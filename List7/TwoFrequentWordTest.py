from easyinput import read

worDic={}
numWords=read(int)
word=read(str)
comp=False
cont=0
while word is not None:
    if word in worDic:
        worDic[word]+=1
    else:
        worDic[word]=1

for i in sorted(worDic.values(),reverse=True):
    if cont==numWords:
        comp=True
        break
    if i>=numWords:
        cont+=1
    else:
        break

if comp:
    print("Hay")
else:
    print("No hay")



    
    
    
