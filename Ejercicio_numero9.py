#9. Crear un programa que genere una matriz de números y la imprima en pantalla.
matriz = [[1,2,3,4,5,6], 
          [1,2,3,4,5,6], 
          [1,2,3,4,5,6], 
          [1,2,3,4,5,6]]
print("Mostrar todos los elementos de la fila ")
for i in matriz:
    print(i)
    
print("Mostrar todos los elementos de las columnas ")
for i in matriz:
    for g in i:
        print(g)

print("Mostrar todos lo elementos de una matriz en su formato ")
for i in matriz:
    for g in i:
        print(g, end= "")
    print ()