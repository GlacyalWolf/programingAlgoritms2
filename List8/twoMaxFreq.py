def max2freq(num:list):
    dic={}
    for i in num:
        if num in dic.keys():
            dic.update({num:dic.get(num)+1})
        else:
            dic.update({num:1})
    
    
    num1=0
    num2=0
    for i in dic:
        






