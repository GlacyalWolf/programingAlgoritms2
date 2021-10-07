def buy_tokens(n):

    '''
    >>> buy_tokens(20)
    (0, 5)
    >>> buy_tokens(50)
    (6, 2)
    >>> buy_tokens(39)
    (5, 1)

    '''
    valorInicial=n;
    cont7=0;
    cont4=0;

    while(n>4):
        n=n-7;
        cont7=cont7+1;
       
        
    while(n%4!=0 ):
        n=n+7;        
        cont7=cont7-1;        
        
    cont4=n//4;   
               

    return(cont7,cont4);


print(buy_tokens(50))