# Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

# - Si el primer número es mayor que el segundo, debe devolver 1.
# - Si el primer número es menor que el segundo, debe devolver -1.
# - Si ambos números son iguales, debe devolver un 0.

# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(num,num1):
    if num > num1 :
        r = 1
    elif num1 > num :
        r = -1
    else :
        r = 0
    return  r

print(relacion(num=5,num1=10))
print(relacion(num=10,num1=5))
print(relacion(num=5,num1=5))