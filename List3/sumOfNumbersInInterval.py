def sum_interval(a,b):
    '''
    >>> sum_interval(5,10)
    45
    >>> sum_interval(1,100)
    5050
    >>> sum_interval(10,20)
    165
    '''

    return(sum(range(a,b+1)));
    
    

print(sum_interval(5,10))
