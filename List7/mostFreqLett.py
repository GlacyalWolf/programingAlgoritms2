from sys import stdin
from pyparsing import Char

from easyinput import *

letDict={}
string=read_line()
while string is not None:
    string=str(string)
    for i in string:
        if i.islower() :
            if i in letDict:
                letDict[i]+=1
            else:
                letDict[i]=1
    string=read_line()


maximum=max(letDict.values())
sortedDic=sorted(letDict)
for i in sortedDic:
    if(letDict[i] == maximum):
        print(f"{i} {maximum}")
        break



