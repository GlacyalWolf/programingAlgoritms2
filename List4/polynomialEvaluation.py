def polynomialEval():
    while(True):
        x=float(input());
        polinom=input().split(" ");
        print (polinom);
        cont=0;
        total=0
        for i in polinom:
            if(cont==0):
                total=total+float(i);
            else:
                total=total+float(i)*pow(x,cont);
            cont+=1;
        print (round(total,4));




polynomialEval()
