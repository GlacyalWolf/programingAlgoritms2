from os import write


times=int(input());
counter=0;

with open("List5/test.txt","w") as testFile:
    for i in range(times):
        testFile.write(input()+"\n");
        

with open("List5/test.txt","r") as testFile:
    for line in testFile:
        serie=line.rstrip("\n").split(" ");
        for i in range(len(serie)-1):
            if(int(serie[i])<int(serie[i+1])):
                counter=counter+1;
        print(counter);
        counter=0;