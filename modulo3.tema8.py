import pandas as pd
import numpy as np
import re

# Paso 1: Carga del Dataset
# Creación de un DataFrame ficticio con datos de ventas
data = {
    'Producto': ['Producto A', 'producto a', 'Producto B', 'Producto C', 'Producto A', None, 'Producto D', 'Producto B', 'Producto E', 'Producto E'],
    'Precio': [10.5, 10.5, 15.0, 20.0, 10.5, np.nan, 25.0, 15.0, 5.0, 5.0],
    'Fecha_Venta': ['2024-01-15', '2024-01-15', '2024-01-16', '2024-01-17', '2024-01-15', '2024-01-18', '2024-01-19', 'not_a_date', '2024-01-20', '2024-01-20'],
    'Región': ['Norte', 'norte', 'Sur', 'Este', 'Norte', 'Oeste', 'Este', 'Sur', 'Oeste', 'Sur']
}
df = pd.DataFrame(data)

# Análisis exploratorio inicial
print("Dataset Original:")
print(df)

# Paso 2: Identificación de Valores Faltantes
print("\nValores Faltantes:")
print(df.isnull().sum())

# Paso 3: Manejo de Valores Faltantes
# Imputación de valores faltantes en 'Precio' con la mediana
df['Precio'].fillna(df['Precio'].median(), inplace=True)

# Paso 4: Eliminación de Duplicados
# Eliminar duplicados basados en las columnas 'Producto' y 'Fecha_Venta'
df.drop_duplicates(inplace=True)

# Paso 5: Corrección de Errores de Consistencia
# Normalización de nombres de productos
df['Producto'] = df['Producto'].str.strip().str.lower().str.replace('producto ', 'Producto ')
# Normalización de la columna 'Región'
df['Región'] = df['Región'].str.strip().str.lower()

# Corrección de errores de formato de fecha
df['Fecha_Venta'] = pd.to_datetime(df['Fecha_Venta'], errors='coerce')

# Paso 6: Validación Final y Exportación
print("\nDataset Limpio:")
print(df)

# Exportar el dataset limpio a un archivo CSV
df.to_csv('dataset_limpio.csv', index=False)
