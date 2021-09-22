def leading_hand(h,m):
    hand="";
    
    if(h>12):
        h=h-12;
    
    if(h>m/5):
        hand="hour hand"
    
    elif(h==m/5):
        hand="draw"
    
    else:
        hand="minute hand"
    
    return hand

print(leading_hand( 4, 20))