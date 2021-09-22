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

    return conect






    
        
        

        


print(str(intersection(1, 4, 4, 6)))