#5. Crear una función que convierta grados Fahrenheit a grados Celsius.

def conversion(f):
    celsius = (f - 32) * 5/9
    return celsius

f = float(input("Ingresa los grados fahrenheit "))
print(f"La conversion de fahrenheit es: {conversion(f)}")