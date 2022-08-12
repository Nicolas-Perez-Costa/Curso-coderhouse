# Escribí un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

a = int(input("Ingrese un numero "))

while (a % 2 == 0) :
    print( "El número", a, "es par.")
    a = int(input("Ingrese otro numero "))
    
print("El número", a, "es impar.")