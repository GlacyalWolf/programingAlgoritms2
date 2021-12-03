def jump(lista,jump):
    
    result=[]

    while len(lista)-lista[jump]>lista[jump]:
        result.append(lista[jump])
        jump=jump + lista[jump]
        print(result)

    return result

print(jump([2, 1, 3, 5, 7, 4, 9, 5, 2, 5, 8], 0))