""" Clase 6 - Ejercicio 11
Brizuela, Ludmila """

import random

class Password:
    __LONGITUD = 8
    __CARACTERES_VALIDOS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

    def __init__(self, longitud=None):
        if longitud is None or longitud < 6 or longitud > 15:
            self.__longitud = self.__LONGITUD
        else:
            self.__longitud = longitud

        self.__contrasena = self.generarPassword()

    def esFuerte(self):
        mayusculas = 0
        minusculas = 0
        numeros = 0
        especiales = 0

        for caracter in self.__contrasena:
            if caracter.isupper():
                mayusculas += 1
            elif caracter.islower():
                minusculas += 1
            elif caracter.isdigit():
                numeros += 1
            else:
                especiales += 1

        return mayusculas > 1 and minusculas > 1 and numeros > 1 and especiales > 0

    # Getters y setters usando el decorador property
    @property
    def longitud(self):
        return self.__longitud

    @longitud.setter
    def longitud(self, nueva_longitud):
        if 6 <= nueva_longitud <= 15:
            self.__longitud = nueva_longitud
            self.__contrasena = self.generarPassword()

    @property
    def contrasena(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, nueva_contrasena):
        self.__contrasena = nueva_contrasena

    def generarPassword(self):
        nueva_contrasena = ''.join(random.choice(self.__CARACTERES_VALIDOS) for _ in range(self.__longitud))
        return nueva_contrasena

    def __str__(self):
        return f"{self.__contrasena} - {self.esFuerte()}"


# Ejemplo de uso
def main():
    passwords = []

    while True:
        longitud = input("Ingrese la longitud de la contraseña (0 para usar el valor por defecto, o 'q' para terminar): ")

        if longitud.lower() == 'q':
            break

        longitud = int(longitud)

        if longitud == 0:
            nueva_password = Password()
        else:
            nueva_password = Password(longitud)

        passwords.append(nueva_password)

    print("Contraseñas generadas: ")
    for i, password in enumerate(passwords, 1):
        print(f"contraseña{i} - {password.esFuerte()}")

if __name__== "__main__":
    main()
