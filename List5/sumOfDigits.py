suma = 0
with open("List5/nums.txt", "w") as f:

    entrada = input()
    while(entrada != ""):
        f.write(entrada+"\n")
        entrada = input()

with open("List5/nums.txt", "r") as f:
    for line in f:
        
        line=line.rstrip()
        cp=line
        line=int(line)
        while(line//10!=0):
            suma=suma+line%10
            line=line//10
            suma=suma+line%10               
            
        suma=str(suma)
        print("The sum of the digits of "+cp+" is "+suma+".")
        suma=0
