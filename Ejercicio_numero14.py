#14. Escribir una función que calcule la media aritmética de una lista de números.

def media_aritmetica(lista):
    total = sum(lista)
    cantidad = len(lista)
    media = total / cantidad
    return media
def main():
    numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    calcular_media = media_aritmetica(numeros)
    print("La media aritmetica es", calcular_media)
main()