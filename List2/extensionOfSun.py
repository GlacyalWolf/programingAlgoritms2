def is_sun_extension(s):

    '''
    >>> is_sun_extension('sun')
    True
    >>> is_sun_extension('assumption')
    True
    >>> is_sun_extension('assume')
    False
    >>> is_sun_extension('russian')
    False
    >>> is_sun_extension('scouting')
    True
    >>> is_sun_extension('innocuous')
    False
    '''
    
    sunysun="";
    for i in s:
        if (i in "sun"):
            sunysun=sunysun+i;
    if("sun" in sunysun):
        return True;
    return False;

print (is_sun_extension("scouting"))
            

