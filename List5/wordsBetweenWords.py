string=input();
string=string.split();

try:
    if(string.index("beginning")<string.index("end") and ("beginning","end " in string)):
        print(string.index("end")-string.index("beginning")-1)
    else:
        print("Error")

except:
    print("Error")