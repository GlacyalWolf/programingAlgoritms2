def descomposition(segundos):
    horas=0;
    min=0;
    while(segundos>=3600):
        horas=horas+1;
        segundos=segundos-3600;

    while(segundos>=60):
        min=min+1;
        segundos=segundos-60;
    return(horas, min, segundos);
    

segundos= int(input("Pon los segundos: "));
print(str(descomposition(segundos)));

