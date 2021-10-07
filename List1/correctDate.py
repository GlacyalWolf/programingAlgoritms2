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
    if m in [1,3,5,7,8,10,12] and 1<=d<=31:
        return True;
    elif m in [4,6,9,11] and 1<=d<=30:
        return True;
    elif m==2 and 1<=d<=28 and leapyear(y) and 1<=d<=29:
        return True;
    
    result=False;    


if __name__ == "__main__":
    import doctest
    doctest.testmod()