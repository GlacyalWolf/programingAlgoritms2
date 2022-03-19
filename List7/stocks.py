
def total_stock(stk1:dict,stk2:dict):
    '''
    >>> stock_alice = {'orange':5, 'lemon':2, 'tangerine':1}
    >>> stock_bob = {'apple':3, 'orange':6, 'tangerine':1}
    >>> stock_alice_bob = total_stock(stock_alice, stock_bob)
    >>> stock_alice_bob == {'tangerine': 2, 'orange':11, 'lemon':2, 'apple':3} 
    True    
    '''
    
    for i in stk1:
        if (i in stk2):
            #stk2.update({i:stk2.get(i)+stk1.get(i)})
            stk2[i]+=stk1[i]
        else:
            #stk2.update({i:stk1.get(i)})
            stk2[i]=stk1[i]
    return stk2
print(total_stock)


    
    
    