# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio.
# Calcula el área de un círculo de 5 de radio
import math
def area_circulo(radio):
    area = math.pi * radio * radio
    return area

print("El area del circulo es:",area_circulo(radio=5))