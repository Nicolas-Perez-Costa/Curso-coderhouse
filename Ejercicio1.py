# Escribí un programa que lea dos números por teclado y permita elegir entre 4 opciones en un menú:

# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
# En caso de no introducir una opción válida, el programa informará de que no es correcta.

#seleccion de numero
a = int(input("Ingrese un número \n"))
b = int(input("Ingrese el segundo número \n"))

#seleccion de opcion de menu
c = int(input("Bienvenido al menú, por favor elija una opcion de 1 a 3 \n"))

#menu con eleccion
if c == 1 :
   print("La suma es: ",a+b) 
elif c == 2:
     print("La resta es: ",a-b)
elif c == 3:
        print("El producto es: ",a*b)
else:
    print("La opcion ingresada no es correcta")