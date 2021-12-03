from easyinput import read

square=[]
squareSize=read(int)

for i in range(squareSize):
    square.append(read(int,amount=squareSize))
    