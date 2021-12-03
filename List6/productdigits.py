import sys


def numdig(n):
    num = 1
    for i in n:
        num = num*int(i)
    return str(num)


num = sys.stdin.readline()

while(num != ""):
    while len(num) > 1:
        prod = numdig(num)

        print(num, prod)
        num = prod
    num = sys.stdin.readline()
