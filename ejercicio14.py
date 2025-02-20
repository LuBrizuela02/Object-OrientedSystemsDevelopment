""" Clase 9 - Ejercicio 14 | Manejo de Excepciones en Python
Brizuela, Ludmila """

class ElementoDuplicadoError(ValueError):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

def agregar_una_vez(lista, elem):
    if elem in lista:
        raise ElementoDuplicadoError(f"Error: Imposible añadir elementos duplicados => {elem}")
    else:
        lista.append(elem)

def main():
    lista_1 = [1, 5, -2]
    agregar = [10, -2, 'hola']

    for valor in agregar:
        try:
            agregar_una_vez(lista_1, valor)
        except ElementoDuplicadoError as e:
            print(f'{e}, {e.__class__}')
    
    print(f'Elementos de la lista: {lista_1} ')

if __name__ == "__main__":
    main()