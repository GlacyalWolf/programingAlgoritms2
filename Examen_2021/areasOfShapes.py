import math;


def area(shape,d1,d2):
    '''
    >>> area('rectangle', 3.1, 4.0)
    12.4
    >>> area('triangle', 6.0, 2.0)
    6.0
    >>> area('rectangle', 8.2, 8.2)
    67.24
    >>> area('circle', 1.0, 0.0)
    3.141592653589793
    '''
    if(shape=="triangle"):
        return float((d1*d2)/2);

    elif(shape=="rectangle"):
        return float(d1*d2);

    elif(shape=="circle"):
        return math.pi*d1**2;
    
