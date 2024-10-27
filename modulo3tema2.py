
# Importamos pandas con el alias pd
import pandas as pd

#ejercicio 1
# Creo una Serie a partir de la lista de asignaturas
asignaturas = ['Matemáticas', 'Ciencias', 'Lengua', 'Sociales']
serie_asignaturas = pd.Series(asignaturas, dtype="string")

# imprimo la serie que se ha creado
print(serie_asignaturas)

#ejercicio 2:inspecciono la serie (múmero, índice y tipos)
# pido imprimir el número de elementos en la serie
print("Tamaño de la serie:", serie_asignaturas.size)

# Imprimo los índices de la serie
print("Índices de la serie:", serie_asignaturas.index)

# Imprimo el tipo de datos de la serie
print("Tipo de datos:", serie_asignaturas.dtype)

#ejercicio 3:creo una serie llamada serie_notas desde el diccionario que se indica ({'Matemáticas': 9.5, 'Ciencias': 8.0, 'Lengua': 7.5, 'Sociales': 6.0})
notas = {'Matemáticas': 9.5, 'Ciencias': 8.0, 'Lengua': 7.5, 'Sociales': 6.0}
serie_notas = pd.Series(notas)
# imprimo la serie creada
print(serie_notas)

#ejercicio 4: accedo al elemento ciencia de la serie llamada serie_notas
# Acceder al valor de 'Ciencias'
print("Nota en Ciencias:", serie_notas['Ciencias'])
