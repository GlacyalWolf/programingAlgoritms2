from easyinput import read  

lista=[]
iteraciones=read(int)

while iteraciones is not None:

    for i in range(0,iteraciones):
        lista.append(read(int))   

    
    lista.reverse()
    
    print(str(lista).strip("[]").replace(",",""))
       
    
    iteraciones=read(int)
    lista=[]
