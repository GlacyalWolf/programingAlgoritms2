def word_count(s):

    '''
    >>> word_count('Qui invenit amicum invenit thesaurum')
    5
    >>> word_count('alea iacta          est')
    3
    >>> word_count('KingKong')
    1
    '''
    cont=0;
    if(len(s)>0 and s[0]!=" "):
        cont=cont+1;

    for i in range(len(s)-1):
        if(s[i]!=" " and s[i+1]==" "):
            cont=cont+1;

    return(cont)   
    

print(word_count('Qui invenit amicum invenit thesaurum'));