# Importo pandas y numpy
import pandas as pd
import numpy as np
#ejercicio 1
# se crea la Serie con las calificaciones y los nombres para tenerlos de índices
calificaciones = pd.Series({'Ana': 8.5, 'Luis': 6.0, 'Marta': np.nan, 'Juan': 7.5, 'Elena': 9.0})

# Accedo a la calificación de Luis
print("Calificación de Luis:", calificaciones['Luis'])

# Accedo a las calificaciones de Marta a Juan usando slicing
print("Calificaciones de Marta a Juan:")
print(calificaciones['Marta':'Juan'])

#ejercicio 2:vamos a obtener resumen
#resumen de la cantidad de calificaciones (calcular y mostrar y no cuenta los NaN)
calificaciones_disponibles = calificaciones.count()
print("Cantidad de calificaciones disponibles:", calificaciones_disponibles)
#resumen de la calificación promedio (calcular y mostrar, ignorar los NaN)
promedio_calificaciones = calificaciones.mean()
print("Calificación promedio:", promedio_calificaciones)
# Resumen estadístico con describe
print("Resumen estadístico de las calificaciones:")
print(calificaciones.describe())


#Ejercicio 3: Operaciones y Funciones en Series

#Multiplico todas las calificaciones por 1.1 para aplicar una curva de calificación y muestro la Serie resultante
calificaciones_curva = calificaciones * 1.1
print("Calificaciones con curva aplicada:")
print(calificaciones_curva)
#Redondeo las calificaciones resultantes del paso anterior a 1 decimal y muestro la Serie resultante
calificaciones_redondeadas = calificaciones_curva.round(1)
print("Calificaciones redondeadas:")
print(calificaciones_redondeadas)

#ejercicio 4: Filtrado y Ordenamiento

#Muestro solo las calificaciones aprobatorias (6.0 o más)
calificaciones_aprobadas = calificaciones[calificaciones >= 6.0]
print("Calificaciones aprobadas:")
print(calificaciones_aprobadas)
#Ordeno las calificaciones de forma ascendente y muestro el resultado
calificaciones_ordenadas = calificaciones.sort_values()
print("Calificaciones ordenadas:")
print(calificaciones_ordenadas)

#Ejercicio 5: Manejo de Datos Desconocidos
#Elimino las calificaciones desconocidas o nulas y muestro la Serie resultante
calificaciones_sin_nan = calificaciones.dropna()
print("Calificaciones sin NaN:")
print(calificaciones_sin_nan)