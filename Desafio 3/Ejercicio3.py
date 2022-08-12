# Escribí un programa que sume todos los números enteros impares desde el 0 hasta el 100:

num = int(1)
suma = int(0)

while num <= 100 :
   if(num % 2 == 0):    
    num = num + 1
   else:
    suma= suma + num
    num = num + 1
print("La suma total es", suma)