from easyinput import *

contVow = 0
contWor = 0



for word in read_many(str):

    for i in word:
        if i in ["a", "e", "i", "o", "u"]:
            contVow += 1
    if contVow % 2 == 0:
        contWor += 1
    contVow = 0


print(contWor)
