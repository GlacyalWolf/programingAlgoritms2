def leapyear(y):
    '''
    >>> leapyear(1999)
    False
    >>> leapyear(1968)
    True
    >>> leapyear(2000)
    True
    >>> leapyear(1800)
    False
    '''
        
    comprovante=True;
    if(y%100!=0 and y%4==0 ):
        comprovante=True;

    elif(y%100==0 and (y//100)%4==0):
        comprovante=True;
    
    else:
        comprovante=False;
    return comprovante


def correct_date(d,m,y):
    '''
    >>> correct_date(30, 11, 1971)
    True
    >>> correct_date(6, 4, 1971)
    True
    >>> correct_date(4, 8, 2001)
    True
    >>> correct_date(29, 2, 2001)
    False
    >>> correct_date(32, 11, 2005)
    False
    >>> correct_date(30, 11, 2004)
    True
    >>> correct_date(-20, 15, 2000)
    False
    '''
    result=False;
    if(m==1 and d<=31):
        result=True;
    
    if(m==2):
        if (leapyear(y) and  d<=29):
            result=True;
        if (not(leapyear(y)) and d<=28):
            result=True;
    
    if(m==3 and d<=31):
        result=True;
    
    if(m==4 and d<=30):
        result=True;

    if(m==5 and d<=31):
        result=True;

    if(m==6 and d<=30):
        result=True;
    
    if(m==7 and d<=31):
        result=True;
    
    if(m==8 and d<=31):
        result=True;
    
    if(m==9 and d<=30):
        result=True;
    
    if(m==10 and d<=31):
        result=True;
    
    if(m==11 and d<=30):
        result=True;
    
    if(m==12 and d<=31):
        result=True;
    
    return result;


if __name__ == "__main__":
    import doctest
    doctest.testmod()