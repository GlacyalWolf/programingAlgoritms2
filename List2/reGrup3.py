def regroup3(s):
    '''
    >>> regroup('r2b2')
    'rb22'
    >>> regroup('a45tr09pw')
    'atrpw4509'
    >>> regroup('nonumbers')
    'nonumbers'
    >>> regroup('543210')
    '543210'
    '''

    stringNum="";
    stringLett="";


    for i in s:
        if i in "0123456789":
            stringNum=stringNum+i;
        else:
            stringLett=stringLett+i; 

    return (stringLett+stringNum);

print(regroup3("asd777wqq"));


    