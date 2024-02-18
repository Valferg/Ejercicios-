#11. Crear un programa que genere una lista de números pares entre 1 y 100.

def generar_lista_pares():
    lis_pares = [numero for numero in range(2, 101, 2)]
    return lis_pares
def main():
    lis_pares = generar_lista_pares()
    print("Lista de nummeros pares entre 1 y 100:", lis_pares)
main()