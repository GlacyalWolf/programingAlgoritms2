import sys
filePath="Exercices_Done_In_Class/protein.pdb"



def countingAtoms(filePath):

    counter=0
    with open(filePath,"r") as f:
        for line in f:
            
            if line.startswith("ATOM") or line.startswith("TER"):
                counter = 1+counter
    return counter


def countingCarbon(filePath):
    counter=0
    with open(filePath,"r") as f:
        for line in f:
            line=line.rstrip()
            if line.startswith("ATOM") or line.startswith("TER") and line.endswith("C"):
                                 counter = 1+counter
    return counter

def countingAnElement(filepath,element):
    counter=0
    element=element.upper()
    with open(filePath,"r") as f:
        for line in f:
            line=line.rstrip()
            if line.startswith("ATOM") or line.startswith("TER") and line.endswith(element):
                
                    counter = 1+counter
    return counter

def whatAtomsAreThere(filepath):
    atomList=[]
    with open(filePath,"r") as f:
        for line in f:
            line=line.rstrip()
            if not(line[-1] in atomList) and line.startswith("ATOM"):
                atomList.append(line[-1])
                

    return atomList


print("Number of atoms:",end=" ")
print(countingAtoms(filePath))

print("Number of carbons:",end=" ")
print(countingCarbon(filePath))

element=sys.stdin.readline().rstrip()

print("Number of "+element.upper()+":",end=" ")
print(countingAnElement(filePath,element))


print(whatAtomsAreThere(filePath))
