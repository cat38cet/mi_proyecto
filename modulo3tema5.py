# Importar pandas
import pandas as pd

# Crear un DataFrame: lo hago con nombre, edad, y salario
data = {
    'Nombre': ['Carlos', 'Ana', 'Pedro', 'Marta'],
    'Edad': [28, 22, 34, 29],
    'Salario': [3000, 3200, 4000, 3500]
}

df = pd.DataFrame(data)

# Explorar los datos usando atributos
print(df.info())     # Información del DataFrame
print(df.shape)      # Dimensiones (filas, columnas)
print(df.size)       # Número total de elementos
print(df.columns)    # Nombres de las columnas
print(df.dtypes)     # Tipos de datos

# Renombrar columnas y reindexar filas
df.rename(columns={'Nombre': 'Empleado', 'Salario': 'Ingreso'}, inplace=True)
df.index = ['ID1', 'ID2', 'ID3', 'ID4']

# Mostrar el DataFrame después de renombrar y reindexar
print(df)

# Acceder a datos específicos usando .loc y .iloc (accedo a la fila por índice y a la tercera fila por posicion)
print(df.loc['ID1'])          
print(df.iloc[2])             

# Añadir una nueva columna con una operación matemática entre columnas existentes
df['Ingreso_Anual'] = df['Ingreso'] * 12

# Mostrar el DataFrame final
print(df)
