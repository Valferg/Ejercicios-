#15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no.

def palindromo(cadena):
    cadena = cadena.lower().replace(" ", " ")
    return cadena == cadena [::-1]

def main():
    cadena2 = input("Ingrese una cadena de texto ")
    if palindromo(cadena2):
        print("Es un palindromo")
    else:
        print("No es un palindromo")
main()