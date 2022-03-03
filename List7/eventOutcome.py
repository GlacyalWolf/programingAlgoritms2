from easyinput import read
scoreList={}
for i in range(read(int)):
    name,score=read(str,int)
    scoreList.update({score:name})


cont=1
for i in sorted(scoreList,reverse=True):
    if cont==1:
        print(f"Gold: {scoreList[i]}")
        cont+=1
    elif cont==2:
        print(f"Silver: {scoreList[i]}")
        cont+=1
    elif cont==3:
        print(f"Bronze: {scoreList[i]}")
        cont+=1
    else:
        print({scoreList[i]})
    

