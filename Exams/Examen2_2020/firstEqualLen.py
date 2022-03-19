from easyinput import *

listalen = []
listalen.append(0)
listaword = []


for word in read_many(str):
    if len(word) in listalen():
        print(listaword[listalen.index(len(word))-1], word)
        break
    listaword.append(word)
    listalen.append(len(word))

if len(word) not in listalen():
    print("All words have diffewrent lenghts")


