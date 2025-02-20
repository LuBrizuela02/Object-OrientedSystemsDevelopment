""" Clase 3 - Ejercicio 5
Brizuela, Ludmila """

def duracion_seg(hs, m, seg):
    """Devuelve el total de segundos."""
    segundos_hs = hs * 3600
    segundos_min = m * 60
    total_seg = segundos_hs + segundos_min + seg
    return total_seg

horas = 2
minutos = 45
segundos = 20

print(f"El total de segundos en el intervalo de {horas} horas {minutos} minutos {segundos} segundos es: ", duracion_seg(horas, minutos, segundos))

