"""Ejercicio3
Brizuela,Ludmila"""

lista = []
contador = 0

while contador < 5:
    valor = int(input("Ingrese un número entero: "))
    lista.append(valor)
    contador += 1

maximo = max(lista)
minimo = min(lista)

print(lista)
print("El número mínimo es: ", minimo)
print("El número máximo es: ", maximo)

