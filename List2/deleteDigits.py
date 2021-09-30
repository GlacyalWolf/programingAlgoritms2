def delete_digits(string):
    '''
    >>> delete_digits('#Pelham 1-2-3#')
    '#Pelham --#'
    >>> delete_digits('7 up')
    ' up'
    >>> delete_digits('92920')
    '''
    arr=[];
    cont=0;
    descarte=[]

    for i in string:
        arr.append(i);
        
        cont=cont+1;    

    for i in range(len(arr)):
        
        if(arr[i]=="0" or arr[i]=="1" or arr[i]=="2" or arr[i]=="3" or arr[i]=="4" or arr[i]=="5" or arr[i]=="6" or arr[i]=="7" or arr[i]=="8" or arr[i]=="9"):
            descarte.append(i);
    
    
            
    for i in descarte:
        arr[i]="";
    
    nuevo="".join(arr);

    return nuevo


            



if __name__ == "__main__":
    import doctest
    doctest.testmod()   

