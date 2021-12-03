from easyinput import *
import sys


def repeated_short(lw):
    '''
    >>> repeated_short(['easy','come','easy','go','will','you','let','me','go'])
    ['easy', 'go']
    >>> repeated_short(['I','can','see','it','can','you','see','it'])
    ['can', 'it', 'see']
    >>> repeated_short(['unbelievable','unbelievable'])
    []
    '''
    listaWord = []
    n = 1
    for i in lw:
        for x in range(n, len(lw)):
            if(i == lw[x] and i not in listaWord and len(i) < 5):
                listaWord.append(i)
        n += 1

    return sorted(listaWord)


for line in read_many_lines():

    words = repeated_short(line.split())
    print(len(words), str(words).strip("[]").replace(",", "").replace("'", ""))
