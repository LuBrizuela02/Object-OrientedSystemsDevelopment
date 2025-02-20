""" Clase 11 - Ejercicio 16
Brizuela, Ludmila """

from peewee import *

# Configuración de la base de datos
db = SqliteDatabase('empleados.db', pragmas ={'journal_mode' : 'wal'})

# Definición de clases/modelos
class BaseModel(Model):
    # Clase base que utilizará la base de datos Sqlite
    class Meta:
        database = db

class Area(BaseModel):
    id = AutoField(primary_key = True)
    nombre_area = CharField(max_length=80, unique=True)

class Empleado(BaseModel):
    id = AutoField(primary_key = True)
    nro_legajo = IntegerField(unique=True, null=False)
    dni = IntegerField(unique=True, null=False)
    nombre = CharField(null=False)
    apellido = CharField(null=False)
    area = ForeignKeyField(Area, backref='empleados')

# Creación de las tablas
def crear_tablas():
    db.connect()
    db.create_tables([Area, Empleado])
    print("Tablas creadas exitosamente.")

# Creación de funciones para el menú
def insertar_empleado():
    # Insertar un registro de empleado
    try:
        nombre_area = input("Ingrese el nombre del área: ")
        nro_legajo = int(input("Ingrese el número de legajo: "))
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        dni = int(input("Ingrese el DNI: "))

        # Buscar o crear el área
        area, creada = Area.get_or_create(nombre_area=nombre_area)

        # Crear el empleado
        Empleado.create(
            nro_legajo = nro_legajo,
            nombre = nombre,
            apellido = apellido,
            dni = dni,
            area = area,
        )
        print("Empleado insertado exitosamente.")
    except IntegrityError as e:
        print("Error: No se pudo insertar el empleado. Verifique los datos.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def seleccionar_empleado_dni():
    # Selecciona un empleado a partir de su número de DNI
    try:
        dni = int(input("Inserte el DNI del empleado: "))
        empleado = Empleado.get(Empleado.dni == dni)
        print(f"Empleado encontrado: {empleado.nombre} {empleado.apellido}, Área: {empleado.area.nombre_area}")
    except Empleado.DoesNotExist:
        print("Empleado no encontrado.")

def seleccionar_todos_empleados():
    # Selecciona todos los empleados de la tabla.
    empleados = Empleado.select()
    if empleados.count() == 0:
        print("No hay empleados registrados.")
    else:
        for empleado in empleados:
            print(f"Legajo: {empleado.nro_legajo}, Nombre: {empleado.nombre} {empleado.apellido}, Área: {empleado.area.nombre_area}")

def modificar_area_empleado():
    # Modifica el área de un empleado a partir de su número de legajo.
    try:
        nro_legajo = int(input("Ingrese el número de legajo del empleado: "))
        nueva_area = input("Ingrese la nueva área: ")

        # Buscar o crear el área
        area, creada = Area.get_or_create(nombre_area = nueva_area)

        # Actualizar el área del empleado
        empleado = Empleado.get(Empleado.nro_legajo == nro_legajo)
        empleado.area = area
        empleado.save()

        print("Área modificada exitosamente.")
    except Empleado.DoesNotExist:
        print("Empleado no encontrado.")

def eliminar_empleado():
    # Elimina un empleado a partir de su número de legajo
    try:
        nro_legajo = int(input("Ingrese le número de legajo del empleado: "))
        empleado = Empleado.get(Empleado.nro_legajo == nro_legajo)
        empleado.delete_instance()
        print("Empleado eliminado exitosamente.")
    except Empleado.DoesNotExist:
        print("Empleado no encontrado.")

# Función principal para ejecutar el programa
def main():
    crear_tablas()

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