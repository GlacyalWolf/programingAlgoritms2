def add_one_day(d,m,y):
    '''   
    >>> add_one_day(12, 3, 2002)
    (13, 3, 2002)
    >>> add_one_day(30, 6, 1975)
    (1, 7, 1975)
    >>> add_one_day(28, 2, 2017)
    (1, 3, 2017)
    >>> add_one_day(15, 6, 1975)[0]
    16
    '''
    d=d+1;
    if(m==2 and d>28 ):
        m=1+m;
        d=1;
    elif(m in (1,3,5,7,8,10,12) and d>31):
        m=1+m;
        d=1;
    elif(m in (4,6,9,11) and d>30):
        m=1+m;
        d=1;
    if(m>12):
        y=1+y;
        m=1;
    return (d,m,y)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)