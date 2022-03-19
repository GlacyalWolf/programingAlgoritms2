def multiple_in_interval(a,b,x):
    '''
    >>> multiple_in_interval(5, 10, 2)
    True
    >>> multiple_in_interval(10, 5, 2)
    False
    >>> multiple_in_interval(10, 10, 2)
    True
    >>> multiple_in_interval(51, 58, 5)
    True
    >>> multiple_in_interval(50, 55, 7)
    False
    >>> multiple_in_interval(100, 180, 92)
    False
    >>> multiple_in_interval(5, 10, 2) and (3>2)
    True
    '''
    for i in range(a,b+1):
        if(x%i==0):
            return True;
        if(i%x==0):
            return True;
    return False;

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

