def middleDigit(numberDigits):
    
    WIN_ANNA="A";
    WIN_BERNARD="B";
    DRAW="=";

    lengthOfDigits=(int(input()))*2;
    stringNum=input();
    listNumbers=stringNum.split(" ");
    refAnt="";
    cont=1;

    for i in stringNum:
        
        if(refAnt!=""):
            if(i[len(i)//2+1]==refAnt[len(i)//2+1]):
                cont+=cont;
                continue;

            if(i[len(i)//2+1]!=refAnt[len(i)//2+1]):
                if(cont%2==0):
                    return WIN_BERNARD;
                else:
                    return WIN_ANNA;
            
            if(len(i)%2==0):
                if(cont%2==0):
                    return WIN_BERNARD;
                else:
                    return WIN_ANNA;


        
        else:
            if(len(i)%2==0):
                return WIN_BERNARD;
        


        
        refAnt=i;

    return DRAW;

    
    

     
middleDigit(3);
