#13. Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y división.

def suma(a,b):
    return a + b
def resta (a,b):
    return a-b
def multiplicacion (a,b):
    return a * b
def division (a,b):
    if b == 0:
        return "No se puede dividir entre cero"
    return a/b
def main():
    numero1 = float(input("Ingrese el primer numero "))
    numero2 = float(input("Ingres en el segundo numero "))
    print("Suma:", suma(numero1, numero2))
    print("Resta:", resta(numero1, numero2))
    print("Multiplicacion:", multiplicacion(numero1, numero2))
    print("Division:", division(numero1, numero2))
main()