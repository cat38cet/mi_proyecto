import pandas as pd
import numpy as np

#1-aplicación de funciones a columnas
# Crear DataFrame df_alturas
df_alturas = pd.DataFrame({'altura_cm': [165, 170, 180, 190, 155]})

# Aplicar función logaritmo natural y crear nueva columna
df_alturas['log_altura'] = df_alturas['altura_cm'].apply(np.log)

# Mostrar DataFrame actualizado
print("Parte 1: df_alturas con logaritmo natural:\n", df_alturas)

#2: Conversión de Columnas a tipo datetime
# Crear DataFrame df_fechas
df_fechas = pd.DataFrame({'fecha_string': ['2022-01-01', '2022-02-01', '2022-03-01']})

# Convertir la columna 'fecha_string' a tipo datetime y renombrar
df_fechas['fecha'] = pd.to_datetime(df_fechas['fecha_string'])

# Eliminar la columna 'fecha_string'
df_fechas.drop(columns=['fecha_string'], inplace=True)

# Mostrar DataFrame actualizado
print("\nParte 2: df_fechas con columna 'fecha' de tipo datetime:\n", df_fechas)

#3-Resumen Descriptivo de un DataFrame
# Obtener resumen estadístico de la columna 'altura_cm'
resumen_altura = df_alturas['altura_cm'].describe()

# Mostrar resumen estadístico
print("\nParte 3: Resumen estadístico de 'altura_cm':\n", resumen_altura)

#4-Eliminación de Columnas en un DataFrame
# Crear DataFrame df_misc
df_misc = pd.DataFrame({
    'A': [10, 20, 30],
    'B': ['x', 'y', 'z'],
    'C': [100.0, 200.0, 300.0]
})

# Eliminar la columna 'B' usando del
del df_misc['B']

# Eliminar la columna 'C' usando pop() y guardarla en una variable
columna_c = df_misc.pop('C')

# Mostrar DataFrame actualizado y contenido de columna 'C'
print("\nParte 4: df_misc sin las columnas 'B' y 'C':\n", df_misc)
print("\nParte 4: Contenido de la columna 'C' eliminada:\n", columna_c)

#5: Operaciones con las Filas de un DataFrame
# Añadir una nueva fila al DataFrame df_misc
nueva_fila = pd.DataFrame({'A': [40]})
df_misc = pd.concat([df_misc, nueva_fila], ignore_index=True)

# Eliminar la primera fila del DataFrame
df_misc.drop(df_misc.index[0], inplace=True)

# Mostrar DataFrame actualizado
print("\nParte 5: df_misc actualizado:\n", df_misc)

#PARTE 2-Gestión Básica de Filas en DataFrames con Pandas
#1: Añadir Filas a un DataFrame
# Crear DataFrame df_productos
df_productos = pd.DataFrame({
    'Producto': ['Laptop', 'Teclado', 'Ratón'],
    'Precio': [1200, 25, 15]
})

# Añadir una nueva fila
nueva_fila_productos = pd.DataFrame({'Producto': ['Monitor'], 'Precio': [250]})
df_productos = pd.concat([df_productos, nueva_fila_productos], ignore_index=True)

# Mostrar DataFrame actualizado
print("\nParte 6.2 - Parte 1: df_productos actualizado:\n", df_productos)

#2: Eliminar Filas de un DataFrame
# Eliminar la primera fila utilizando drop()
df_productos.drop(df_productos.index[0], inplace=True)

# Mostrar DataFrame actualizado
print("\nParte 6.2 - Parte 2: df_productos sin la primera fila:\n", df_productos)

#3: Filtrar Filas en un DataFrame
# Añadir una columna 'En Stock' con valores booleanos
df_productos['En Stock'] = [True, False, True, True]

# Filtrar productos en stock con precio mayor a 20
productos_filtrados = df_productos[(df_productos['En Stock'] == True) & (df_productos['Precio'] > 20)]

# Mostrar productos filtrados
print("\nParte 6.2 - Parte 3: Productos en stock con precio mayor a 20:\n", productos_filtrados)

#4: Ordenar un DataFrame
import pandas as pd
import numpy as np

# Parte 4: Ordenar un DataFrame
import pandas as pd

# Crear el DataFrame
df_productos = pd.DataFrame({
    'Producto': ['Producto A', 'Producto B', 'Producto C'],
    'Precio': [15, 30, 20],
    'En Stock': [True, False, True]
})

# Mostrar el DataFrame original
print("DataFrame original:\n", df_productos)

# Ordenar el DataFrame por la columna 'Precio' en orden ascendente
df_productos_sorted = df_productos.sort_values(by='Precio').reset_index(drop=True)

# Mostrar el DataFrame ordenado
print("\nDataFrame ordenado por 'Precio':\n", df_productos_sorted)

#5: Manejar Datos Desconocidos en un DataFrame
# Añadir una fila con un producto nuevo pero sin precio (NaN)
nueva_fila_nan = pd.DataFrame({'Producto': ['Tablet'], 'Precio': [np.nan], 'En Stock': [True]})
df_productos = pd.concat([df_productos, nueva_fila_nan], ignore_index=True)

# Eliminar filas con valores desconocidos (NaN)
df_productos_sin_nan = df_productos.dropna()

# Mostrar DataFrame actualizado sin NaN
print("\nParte 6.2 - Parte 5: df_productos sin valores desconocidos:\n", df_productos_sin_nan)
