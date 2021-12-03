from easyinput import read
x=read(int)
while x is not None:    
    listint = []    
    for i in range(x):
        listint.append(read(int))
    print(max(listint))
    
    x=read(int)
    
