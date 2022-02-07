from easyinput import read

antNum=None
platLen,num=read(int,int)
cont=1
response=True

while num is not None:
    
    if (num==antNum):        
        cont+=1
    
    elif (num!=antNum):
        cont=1
    
    if cont==platLen:
        print (f"A plateu of {num}'s at least {platLen} occurs.")
        response=False
        break
    
    antNum=num
    num=read(int)
    
if response:
    print(f"No plateau of length {platLen} occurs.")

