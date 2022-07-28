# Escribí un programa que pida al usuario cuantos números quiere introducir. 
# Luego lee todos los números y realiza una media aritmética:

#solicito al usuario que ingrese la cantidad de numeros que quiere introducir

num = int(input("Introduzca la cantidad de numeros que quiere ingresar \n"))
list_num = []
t = int(0)

#solicito los numeros y los guardo en una lista
while t < num :
    list_num.append(input("Ingrese un numero \n"))
    t+=1

#muestro la lista
print(list_num)

#ejecuto y muestro la media aritmetica
sumT = int(0)
for numero in list_num:
    sumT+=int(numero)
prom = float(sumT/len(list_num))
print(prom)