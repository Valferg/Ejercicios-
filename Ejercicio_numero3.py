#3. Crear un programa que genere una lista de números aleatorios y los imprima en pantalla.

import random

def generar_lista_numeros_aleatorios(longitud, minimo, maximo):
    lista_numeros = [random.randint(minimo, maximo) for _ in range(longitud)]
    return lista_numeros

longitud_lista = 10
valor_minimo = 1
valor_maximo = 100
numeros_aleatorios = [random.randint(valor_minimo, valor_maximo) for _ in range(longitud_lista)]
print("Lista de números aleatorios:", numeros_aleatorios)