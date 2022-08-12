# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas.
# La primera con los números pares, y la segunda con los números impares:
# 🖐 Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

def separar(list):
    lP = []
    lI = []
    for elemento in list :
        if (elemento%2) == 0 :
            lP.append(elemento) 
        else :
            lI.append(elemento) 
    lP.sort()
    lI.sort()     
    return  lP,lI

listaPrueba = [0,9,5,4,2,6,8,7,3,1]

print(separar(listaPrueba))