def is_univariate_word(s):
    '''
    >>> is_univariate_word('xxXxxxXX')
    True
    >>> is_univariate_word('xyyyyYYY')
    False
    >>> is_univariate_word('y')
    True
    >>> is_univariate_word('yyyyx')
    False
    '''
    s=str.lower(s);
    comp=s[0];
    ret=True;

    for i in s:
        if(comp!=i):
            ret=False;
    
    return ret;

if __name__ == "__main__":
    import doctest
    doctest.testmod() 

    