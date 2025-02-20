""" Clase 4 - Ejercicio 8
Brizuela, Ludmila """

class Persona:
    def __init__(self, nombre, edad, dni):
        # Creación de atributos privados
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Método que retorna la edad
    def mostrar_edad(self):
        return self.__edad

    # Método que retorna si es mayor de edad
    def es_mayor_edad(self):
        return self.__edad >= 18

# Ejemplo
persona1 = Persona("Ludmila", 22, "44205889")

print(persona1.mostrar_edad())
print(persona1.es_mayor_edad())
