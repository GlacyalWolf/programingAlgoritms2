from easyinput import *
import easyinput

line = easyinput.read_line()
comp = False

while line is not None:

    line = str(line).split()
    cont = len(line)
    for i in line:
        if "a" in i and "e" in i and "i" in i and "o" in i and "u" in i:
            cont -= 1
            if cont == 0:
                comp = True

        else:
            break

    if comp:
        print(" ".join(line))
        break

    line = easyinput.read_line()

if not comp:
    print("No all-pentavocalic line was found")
