def walker(x,y,steps):
    '''
    >>> walker(4, 1, 'NEENWNWWS')
    (3, 3)
    >>> walker(3, 5, 'NESW')
    (3, 5)
    >>> walker(0, 4, 'SSSSEWEWNNNN')
    (0, 4)
    >>> walker(0, 0, 'SWSWNES')
    (-1, -2)
    >>> walker(6, 3, '')
    (6, 3)
    '''
    for i in steps:
        if(i=="N"):
            y=y+1;
        elif(i=="S"):
            y=y-1;
        elif(i=="E"):
            x=x+1;
        elif(i=="W"):
            x=x-1;
    return (x,y);

