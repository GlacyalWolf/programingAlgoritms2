import sys


def trigram(word):
    listTri = []
    index = 0
    trhe = ""
    
    while index+2 < len(word):

        for i in range(index, index+3):
            trhe += word[i]

        listTri.append(trhe)
        trhe = ""
        index += 1

    return listTri


def somethingInCmon(word1, word2):
    listWord1 = trigram(word1)
    listWord2 = trigram(word2)

    for i in listWord1:
        for x in listWord2:
            if i == x:
                return True
    return False


listaWords = sys.stdin.readline().rstrip().split()


'''inde=0
for i in listaWords:
    for x in range(inde+1,len(listaWords)):
        if somethingInCmon(i,listaWords[x]):
            print(i,listaWords[x])
            break

    inde+=1'''


memo = ""
for i in listaWords:
    if somethingInCmon(memo, i):
        print(memo, i)
    memo = i
