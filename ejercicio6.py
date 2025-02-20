""" Clase 3 - Ejercicio 6
Brizuela, Ludmila """

def duracion_seg(hs, m, seg):
    """Devuelve el total de segundos."""
    segundos_hs = hs * 3600
    segundos_min = m * 60
    total_seg = segundos_hs + segundos_min + seg
    return total_seg

print("Ingrese el primer intervalo de tiempo.")
horas1 = int(input("Horas: "))
minutos1 = int(input("Minutos: "))
segundos1 = int(input("Segundos: "))

print("Ingrese el segundo intervalo de tiempo: ")
horas2 = int(input("Horas: "))
minutos2 = int(input("Minutos: "))
segundos2 = int(input("Segundos: "))

"""Calculo la duración total en segundos de ambos intervalos"""
intervalo1_segundos = duracion_seg(horas1, minutos1, segundos1)
intervalo2_segundos = duracion_seg(horas2, minutos2, segundos2)

total_segundos = intervalo1_segundos + intervalo2_segundos

"""Convierto los segundos a horas, minutos y segundos"""
horas_total = total_segundos // 3600
minutos_total = (total_segundos % 3600) // 60
segundos_total = total_segundos % 60

print(f"La suma de los dos intervalos da una duración total de {horas_total} horas {minutos_total} minutos y {segundos_total} segundos.")
