""" Clase 4 - Ejercicio 9
Brizuela, Ludmila """

class ListaDeTareas:
    # Atributo de instancia privado de tipo list
    def __init__(self):
        self.__lista_tareas = []

    # Agregar una tarea a la lista
    def agregarTarea(self, tarea):
        if tarea: # Verifica que tarea exista
            self.__lista_tareas.append(tarea)
            return "Tarea agregada correctamente a la lista"
        else:
            return "La tarea no fue agregada a la lista"

    # Eliminar una tarea de la lista
    def quitarTarea(self, tarea):
        if tarea in self.__lista_tareas:
            self.__lista_tareas.remove(tarea)
            return "Tarea eliminada correctamente de la lista"
        else:
            return "La tarea no fue eliminada de la lista"

    # Mostrar tareas de la lista
    def mostrarTareas(self):
        return self.__lista_tareas

if __name__ == '__main__':
    mi_lista = ListaDeTareas()

    # Agregar tareas
    print(mi_lista.agregarTarea("Estudiar para el examen"))
    print(mi_lista.agregarTarea("Ir al gimnasio"))
    print(mi_lista.agregarTarea("Ordenar la habitación"))

    # Mostrar lista de tareas
    print(mi_lista.mostrarTareas())

    #Eliminar una tarea
    print(mi_lista.quitarTarea("Ir al gimnasio"))

    # Mostrar nueva lista de tareas
    print(mi_lista.mostrarTareas())
