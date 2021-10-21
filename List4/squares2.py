def squares2():
    cont=0;

    while(True):
        n=input();
        
        print("");
        if(n!=""):       
        
            n=int(n);
            for i in range(n):
                for i in range(n):
                    print(cont,end="");
                    cont+=1;
                    if(cont>9):
                        cont=0;
                print("");
            print("");
        else:
            break;
        cont=0;
squares2();