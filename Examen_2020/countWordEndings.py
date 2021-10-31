def count_word_endings(wordList):
    '''
    >>> count_word_endings( ('dog', 'cat', 'birds', 'reached', 'eat') )
    (1, 1, 2)
    >>> count_word_endings( ('dog', 'had', 'cat', 'reached') )
    (0, 2, 1)
    >>> count_word_endings( ('dog', 'fog', 'why', 'not') )
    (0, 0, 1)
    >>> sum( count_word_endings( ('dog', 'had', 'cat', 'reached') ) )
    3
    '''

    #Write a function count_word_endings(x) that receives a tuple x of words, and returns how many of them end in ‘s’, 
    # how many end in ‘d’, and how many end in ‘t’.
    
    s=0;
    d=0;
    t=0;

    for i in wordList:
        lastLeter=str.lower((i[len(i)-1]));
        if(lastLeter=="s"):
            s=s+1;

        elif(lastLeter=="d"):
            d=d+1;
            
        
        elif(lastLeter=="t"):
            t=t+1;           


    
    return (s,d,t);

print(count_word_endings(('dog', 'cat', 'birds', 'reached', 'eat')))
        

