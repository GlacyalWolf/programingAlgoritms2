from easyinput import read

word=read(str)
wordLenDic={}
while word is not None:
    long=len(word)
    if(len(word) in wordLenDic.keys()):

        oneWordAdd={long:wordLenDic.get(long)+[word]}
        wordLenDic.update(oneWordAdd)

    else:

        oneWordAdd={long:[word]}
        wordLenDic.update(oneWordAdd)
    word=read(str)




