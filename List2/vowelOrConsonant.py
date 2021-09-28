def vowel_consonant_count(string):
    '''
    >>> vowel_consonant_count("SpartacUs")
    (3, 6)
    >>> vowel_consonant_count("KingKong")
    (2, 6)
    '''
    vowel=0;
    consonant=0;
    string=str.lower(string);
    for i in string:
        if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            vowel=vowel+1;
        else:
            
            consonant=consonant+1;
    
    return (vowel,consonant)
        





if __name__ == "__main__":
    import doctest
    doctest.testmod()   
    