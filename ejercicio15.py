""" Clase 10 - Ejercicio 15
Brizuela, Ludmila """

import sqlite3

# Conexión a la base de datos
def conectar_bd():
    bd = sqlite3.connect("empleados.db")
    print("Base de datos abierta")
    return bd

# Creación de la tabla
def crear_tabla():
    bd = conectar_bd()
    cursor = bd.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS empleados (
                        "id"	INTEGER PRIMARY KEY AUTOINCREMENT,
                        "nro_legajo"	INTEGER NOT NULL UNIQUE,
                        "dni"	INTEGER NOT NULL UNIQUE,
                        "nombre"	TEXT NOT NULL,
                        "apellido"	TEXT NOT NULL,
                        "area"  TEXT NOT NULL
                    );''')
    bd.commit()
    bd.close()

# Función para insertar un registro de empleado
def insertar_empleado():
    bd = conectar_bd()
    cursor = bd.cursor()
    try:
        nro_legajo = int(input("Ingrese el número de legajo: "))
        dni = int(input("Ingrese el DNI: "))
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        area = input("Ingrese el área: ")
        cursor.execute("INSERT INTO empleados (nro_legajo, dni, nombre, apellido, area) VALUES (?, ?, ?, ?, ?)",
                        (nro_legajo, dni, nombre, apellido, area))
        bd.commit()
        print("Empleado insertado correctamente.")
    except sqlite3.IntegrityError:
        print("Error: El número de legajo o el DNI ya existen.")
    finally:
        bd.close()

# Función para seleccionar un empleado por DNI
def seleccionar_empleado_dni():
    bd = conectar_bd()
    cursor = bd.cursor()
    dni = int(input("Inserte el DNI del empleado: "))
    cursor.execute("SELECT * FROM empleados WHERE dni = ?", (dni,))
    empleado = cursor.fetchone()
    bd.close()
    if empleado:
        print("Empleado encontrado: ", empleado)
    else:
        print("Empleado no encontrado.")

# Función para seleccionar todos los empleados
def seleccionar_todos_empleados():
    bd = conectar_bd()
    cursor = bd.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleados = cursor.fetchall()
    bd.close()
    if empleados:
        print("Lista de empleados: ")
        for empleado in empleados:
            print(empleado)
    else:
        print("No hay empleados registrados.")

# Función para modificar el area de un empleado en función de su nro de legajo
def modificar_area_empleado():
    bd = conectar_bd()
    cursor = bd.cursor()
    nro_legajo = int(input("Ingrese el número de legajo del empleado: "))
    nueva_area = input("Actualice el área del empleado: ")
    cursor.execute("UPDATE empleados SET area = ? WHERE nro_legajo = ?", (nueva_area, nro_legajo))
    if cursor.rowcount == 0:
        print("Empleado no encontrado.")
    else:
        bd.commit()
        print("Área actualizada correctamente.")
    bd.close()

# Función para eliminar un empleado a partir del nro de legajo
def eliminar_empleado():
    bd = conectar_bd()
    cursor = bd.cursor()
    nro_legajo = int(input("Ingrese el número de legajo del empleado a eliminar: "))
    cursor.execute("DELETE FROM empleados WHERE nro_legajo = ?", (nro_legajo,))
    if cursor.rowcount == 0:
        print("Empleado no encontrado.")
    else:
        bd.commit()
        print("Empleado eliminado correctamente.")
    bd.close()

# Función principal para ejecutar el programa
def main():
    crear_tabla()
    while True:
        print("\nSeleccione una opción:")
        print("1 - Insertar un registro de empleado")
        print("2 - Seleccionar un registro de empleado por DNI")
        print("3 - Seleccionar todos los empleados")
        print("4 - Modificar el área de un empleado por número de legajo")
        print("5 - Eliminar un empleado por número de legajo")
        print("6 - Finalizar")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            insertar_empleado()
        elif opcion == "2":
            seleccionar_empleado_dni()
        elif opcion == "3":
            seleccionar_todos_empleados()
        elif opcion == "4":
            modificar_area_empleado()
        elif opcion == "5":
            eliminar_empleado()
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()