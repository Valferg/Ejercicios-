#2. Escribir una función que calcule el área de un círculo dado su radio.

import math
print("Ingrese el radio del circulo ")
radio = float(input())
Area = math.pi * (radio * radio)
print("El area del circulo con el radio es ",radio, "es: ",round (Area, 2))