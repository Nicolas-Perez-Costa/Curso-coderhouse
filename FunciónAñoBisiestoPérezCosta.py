def anioBisiesto(anio) :

    if anio.isnumeric():
        anio = int(anio)
        if anio % 4 == 0 and anio % 100 != 0 :
            resultado = print(anio,"es año bisiesto.\n")
        elif anio % 100 == 0 and anio % 400 == 0 :
            resultado = print(anio,"es año bisiesto.\n")
        else :
            resultado = print(anio,"no es año bisiesto.\n")     
        return resultado
    else:
        resultado = print("La variable no es numerica.")
    return resultado

        
anio = input("Ingrese el año:\n")

anioBisiesto(anio)