from easyinput import read
cont = 0
listnum = []

iter = read(int)

for i in range(iter):
    listnum.append(read(int))

for i in listnum:
    if(listnum[-1] == i):
        cont += 1
cont-=1
print(cont)
