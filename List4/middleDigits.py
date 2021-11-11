

WIN_ANNA="A";
WIN_BERNARD="B";
DRAW="=";



def x():  
        
    repetitions=int(input())*2
    num=input();
    memoNum=num;

    for i in range(repetitions):
        
        if(len(num)%2!=0):           
            
            if(memoNum[(len(memoNum)//2)]!=num[(len(num)//2)]):
                if(i%2!=0):
                    return WIN_ANNA;
                else:
                    return WIN_BERNARD;

        else:
            if (i==0):
                return WIN_BERNARD;
            elif(i%2!=0):
                return WIN_ANNA;
            else:
                return WIN_BERNARD;
        
        memoNum=num;
        num=input();
    return DRAW;


print(x())


        






    


