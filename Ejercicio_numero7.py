#7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada.

lista = []
cantidad = int(input("Ingrese los numeros que desee "))
i = 1
while (i <= cantidad):
    n = int(input(f"{i} Ingrese un numero "))
    lista.append(n)
    i+=1

print("El numero mayor es", max (lista))
print("El numero menor es", min (lista))