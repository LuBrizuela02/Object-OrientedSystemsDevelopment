""" Clase 3 - Ejercicio 7
Brizuela, Ludmila """
# Escribir una función que reciba una muestra de números en una lista y retorne su media.

def lista_media(valores):
    if valores == 0:
        return 0
    else:
        suma = sum(valores)
        media = suma // len(valores)
        return media

valores = [18, 19, 19, 20, 22, 24, 24]
resultado = lista_media(valores)

print(f"La media de la lista de números es {resultado}.")
