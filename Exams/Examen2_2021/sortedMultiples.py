from easyinput import *
intList = []


for num in read_many(int):

    if num % 7 == 0:
        intList.append(num)


intStr = str(sorted(intList)).strip("[]").replace(",", "")

if(intStr != ""):
    print("Multiples of 7: "+intStr)

else:
    print("No multiples of 7")
