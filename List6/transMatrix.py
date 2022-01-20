'''
def transpose(m: list) -> None:
    ma2=[]
    for y in range(len(m)):
        col=[]
        for x in range(len(m)):
            col.append(m[x][y])
        ma2.append(col)
    m=ma2
'''

def transpose(m: list) -> None:
    n=len(m)
    
    for i in range(n-1):
        for x in range(i+1,n):
            m[i][x],m[x][i]=m[x][i],m[i][x]

        
     


ma=[[1,2,3],[4,5,6],[7,8,9]]
transpose(ma)
print(ma)


