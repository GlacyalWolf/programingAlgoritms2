def minMax(m: list) -> list:
    mm=[]
    for x in m:
        row=[]
        row.append(min(x))
        row.append(max(x))
        mm.append(row)
    return mm

ma=[[1,2,3],[4,5,6],[7,8,9]]
print(minMax(ma))