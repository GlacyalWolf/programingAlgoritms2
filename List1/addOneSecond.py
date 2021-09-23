## h < 24, m < 60 and s < 60,
def add1sec(h,m,s):
    result=[];
    if(h < 24 and m < 60 and s < 60):
        s=s+1;
        if(s>59):
            s=0;
            m=m+1;
        if(m>59):
            
            m=0;
            h=h+1;
        if(h>23):
            h=0;
    result=[h,m,s];
    return result;

print (add1sec(12, 59, 59));
        