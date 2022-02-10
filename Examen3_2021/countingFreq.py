from easyinput import read


dictToFill = {}
# save all nums in a dictionari
for i in range(read(int)):
    num = read(int)
    # if the key exist
    if(num in dictToFill.keys()):

        dictToFill.update({num: dictToFill.get(num)+1})
    # if the key doesn't exist
    else:
        dictToFill.update({num: 1})

order = sorted(dictToFill.keys())
# print the dictionari x : y
for i in order:
    print(f"{i} : {dictToFill.get(i)}")
