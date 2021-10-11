def count_a(s,stop):
    '''
    >>> count_a('naturally', 'u')
    1
    >>> count_a('russian', 't')
    -1
    >>> count_a('adaptation', 'a')
    0
    >>> count_a('adaptation', 'n')
    3
    '''
    numberOfA=-1;
    if (stop not in s):
        return numberOfA;
    numberOfA=0;
    for i in s:
        
        if (i==stop):            
            return numberOfA;
        if (i=="a"):
            numberOfA=numberOfA+1;


print(count_a('adaptation', 'a'))