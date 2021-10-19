def temperature():
    COLD="it's cold";
    HOT="it's hot";
    OK="it's ok";
    BOIL="water would freeze";
    FREEZ="water would boil";
    temp=int(input());

    if(temp>30):
        print(HOT);
        if(temp>=100):
            print(BOIL);
                 
    elif(temp<10):
        print(COLD);
        if(temp<=0):
            print(FREEZ);
    else:
        print(OK);

temperature();