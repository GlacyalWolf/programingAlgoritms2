def collatz(n):
    cont=0;

    while(n>1):
        
        cont=cont+1
        if(n%2==0):
            n=n/2;

        else:
            n=(n*3)+1;
    return cont;

print(collatz(int(input())));
