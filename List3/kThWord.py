def kth_word(s,k):
    '''
    >>> kth_word('Alea iacta est', 3)
    'est'
    >>> kth_word('Alea iacta est', 1)
    'Alea'
    >>> kth_word('KingKong', 2)
    ''
    '''

    ret="";
    cont=0;

    if(len(s)>0 and s[0]!=" "):
        cont=cont+1;

    for i in range(len(s)):
        if(cont==k and s[i]!=" "):
            ret=ret+s[i];
        if(i==len(s)-1):
            return (ret);
        if(s[i]!=" " and s[i+1]==" "):
            cont=cont+1;
    return(ret);
        

      
            
        

print(kth_word('KingKong', 2))