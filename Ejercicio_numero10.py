#10. Escribir una función que calcule el factorial de un número dado.

def factorial(numero):
    if (numero < 0):
        return None
    resultado = 1
    for i in range (1, numero + 1):
            resultado = numero * i
    return resultado
def main():
    numero = int(input("Ingrese un numero "))
    resultado_fact = factorial(numero)
    if (resultado_fact is not None):
        print("El factorial de", numero, "es:", resultado_fact)
    else:
         print("Error: Se debe ingresar un numero entero positivo")
main()