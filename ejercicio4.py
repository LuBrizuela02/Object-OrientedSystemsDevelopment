"""Ejercicio4
Brizuela,Ludmila"""

lista = []

for i in range(5):
    valor = int(input("Ingrese un número entero: "))
    lista.append(valor)

if len(lista) != len(set(lista)):
    print("HAY DUPLICADOS")
else:
    print("SON TODOS DISTINTOS")
