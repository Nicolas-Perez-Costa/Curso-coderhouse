# Escribí un programa que pida al usuario un número entero del 0 al 9, 
# y que mientras el número no sea correcto se repita el proceso. 
# Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:

numeros = [1, 3, 6, 9]
num = int(input("Ingrese un numero del 0 al 9: \n"))

#filtro el numero
while num < 0 or num > 9 :
    num = int(input("El numero ingresado es incorrecto, por favor vuelva a intentarlo. \n"))
else:
    #recorro la lista y compruebo
    onList = bool(False)
    for numero in numeros:
        if numero == num:
            onList = True 
            break
        else:
            onList = False
    if onList:
        print("El numero esta en la lista. \n")
    else:
        print("El numero no esta en la lista. \n")

