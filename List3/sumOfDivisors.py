def sum_divisors(a):

    '''
    >>> sum_divisors(1)
    0
    >>> sum_divisors(2)
    1
    >>> sum_divisors(6)
    6
    >>> sum_divisors(15)
    9
    >>> sum_divisors(24)
    36
    >>> sum_divisors(28)
    28
    >>> sum_divisors(47)
    1
    '''
    total=0;
    

    for i in range(1,a):
        if(a%i==0):
            total=total+i;
    
    return (total);

print(sum_divisors(47));
