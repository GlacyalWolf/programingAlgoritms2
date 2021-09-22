def grade(mark):
    nota="";
    if(mark<5):
        nota="suspens"
    elif(mark<7):
        nota="aprovat"
    elif(mark<9):
        nota="notable"
    elif(mark<10):
        nota="excel.lent"
    else:
        nota="MH"
    
    return nota;

print(grade(10))