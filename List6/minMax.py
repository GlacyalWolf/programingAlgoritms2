def minMax(m: list) -> list:
    mm=[]

    for x in range(len(m)):
        col=[]
        
        sum=[]
        for y in range(len(m)):
            
            col.append(m[y][x])
        sum.append(min(m[x]))
        sum.append(max(col))
        mm.append(sum)
    return mm

        



ma=[[1,2,-3],[4,5,6]]
print(minMax(ma))

