""" Clase 5 - Ejercicio 10
Brizuela, Ludmila """

import random

class Password:
    # Atributos de Clase Privados
    __LONGITUD = 8
    __CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    # Atributos de Instancia Privados
    def __init__(self, longitud=None):
        # Si no se proporciona una longitud o está fuera del rango, usará el valor por defecto
        if longitud is None or longitud < 6 or longitud > 15:
            self.__longitud = self.__LONGITUD
        else:
            self.__longitud = longitud

        # Genera la contraseña al crear el objeto
        self.__contrasena = self.generarPassword()

    # Métodos de Instancia Públicos
    def esFuerte(self):
        # Cuenta los tipos de caracteres en la contraseña
        mayusculas = 0
        minusculas = 0
        numeros = 0
        especiales = 0

        # Verifica los criterios para cada caracter en la contraseña
        for caracter in self.__contrasena:
            if caracter.isupper():
                mayusculas += 1
            elif caracter.islower():
                minusculas += 1
            elif caracter.isdigit():
                numeros += 1
            else:
                especiales += 1

        # Verifica si cumple los criterios de una contraseña fuerte
        return mayusculas > 1 and minusculas > 1 and numeros > 1 and especiales > 0

    def generarPassword(self):
        # Genera una contraseña aleatoria
        nueva_contrasena = ""
        for _ in range(self.__longitud):
            nueva_contrasena += random.choice(Password.__CARACTERES_VALIDOS)
        return nueva_contrasena

    # Métodos públicos getters y setters
    def getLongitud(self):
        return self.__longitud

    # Actualiza la longitud y genera una nueva contraseña
    def setLongitud(self, nueva_longitud):
        if 6 <= nueva_longitud <= 15:
            self.__longitud = nueva_longitud
            self.__contrasena = self.generarPassword()

    def getContrasena(self):
        return self.__contrasena

    def __str__(self):
        return f"{self.__contrasena} - {self.esFuerte()}"


# Ejemplo de uso

# Lista para almacenar las contraseñas
passwords = []

# Bucle para crear contraseñas
while True:
    longitud = input("Ingrese la longitud de la contraseña (0 para usar el valor por defecto, o 'q' para terminar): ")

    # Salir del bucle si el usuario ingresa 'q'
    if longitud.lower() == 'q':
        break

    longitud = int(longitud)

    if longitud == 0:
        # Crea una contraseña con la longitud por defecto
        nueva_password = Password()
    else:
        # Crea una contraseña con la longitud especificada
        nueva_password = Password(longitud)

    # Agrega la nueva contraseña a la lista
    passwords.append(nueva_password)

# Mostrar cada una de las contraseñas creadas y si es o no fuerte
print("Contraseñas generadas: ")
for i, password in enumerate(passwords, 1):
    print(f"contraseña{i} - {password.esFuerte()}")
