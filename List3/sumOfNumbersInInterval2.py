def sum_interval(a,b,n):

    '''
    >>> sum_interval(5,10,8)
    8
    >>> sum_interval(5,10,3)
    0
    >>> sum_interval(1,100,6)
    510
    >>> sum_interval(10,20,0)
    30
    '''

    total=0;

    for i in range(a,b+1):
        i=str(i);
        if(i[len(i)-1])==str(n):
            total=total+int(i);
    
    return total;

print(sum_interval(5,10,8))

