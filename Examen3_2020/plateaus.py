from easyinput import read

antNum=None
platLen,num=read(int,int)
cont=0
while num is not None:
    
    if (num==antNum):
        
        cont+=1
    
    if cont==platLen:
        print ("hola")
        break
    


    
    
    antNum=num
    num=read(int)
    
    