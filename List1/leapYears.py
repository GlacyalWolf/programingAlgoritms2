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


if __name__ == "__main__":
    import doctest
    doctest.testmod()

