def intersection(a,b,c,d):
    conect=[]
    if(a>=c):
        conect.append(a)
    else:
        conect.append(c)
    
    if(b<=d):
        conect.append(b)
    else:
        conect.append(d)

    if(conect[0]>conect[1]):
        conect=[False,1,0]
    else:
        conect.insert(0,True)
    return conect  
      


print(str(intersection(10, 16, 12, 15 )))