def nondec(num):
    ''' 
    >>> nondec(113355779)
    True
    >>> nondec(44569)
    True
    >>> nondec(346234)
    False
    >>> nondec(222)
    True
    '''
    num=str(num);
    for i in range(len(num)):

        if(i+1<len(num)):

            if(int(num[i])>int(num[i+1])):
                return (False);
                
    return (True);

