from easyinput import read

word=read(str)
suflist={}
while word is not None:
    
    suf=word[-3:]

    if len(word)>2:
        if(suf in suflist and word not in suflist[suf]):
            suflist[suf]+=[word]
        else:
            suflist[suf]=[word]
    word=read(str)


for i in sorted(suflist):
    lenlist=len(suflist[i])
    if (lenlist>1):
        print(f"{i}: {lenlist} "+" ".join(suflist.get(i)))
