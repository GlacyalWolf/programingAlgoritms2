def lowupp(info):
    '''
    >>> lowupp('_Hi There!')
    'hi there!'
    >>> lowupp('^Hi There!')
    'HI THERE!'
    >>> lowupp('Hi There!')
    'Hi There!'
    '''
    retString="";
    if(info[0]=="^"):
        for i in info:
            if(i!="^"):
                retString=retString+i;
        return str.upper(retString);
    
    elif(info[0]=="_"):
        for i in info:
            if(i!="_"):
                retString=retString+i;
        return str.lower(retString);
    else:
        return info;
    



