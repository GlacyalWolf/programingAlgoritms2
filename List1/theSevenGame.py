def winner(p,q,r,s):
    '''
    >>> winner(1, 3, 5, 3)
    1
    >>> winner(2, 4, 4, 3)
    2
    >>> winner(1, 3, 2, 3)
    2
    >>> winner(2, 4, 3, 3)
    0
    >>> winner(4, 4, 5, 6)
    0
    '''
    
    if(p,q,r,s >0 and p,q,r,s < 6):
        
        player1=p+q;
        player2=r+s;        

        if(player1>player2 ):            
            winner=1;        
        
        if(player2>player1 ):
            winner=2;

        if(player1>7):
            winner=2;

        if(player2>7):
            winner=1;

        if(player2 and player1 > 7 or player1==player2):
            winner=0;       
    
    return winner

if __name__ == "__main__":
    import doctest
    doctest.testmod()



