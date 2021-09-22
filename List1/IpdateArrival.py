def update_arrrival(h, m, d):
    while(d>1):
        m=m+1;
        if(m>=60):
            h=h+1;
            m=1;
        if(h>23):
            h=0;
        d=d-1;
    return(h, m)

print(str(update_arrrival(12, 30, 60)))