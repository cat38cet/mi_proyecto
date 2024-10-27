import pandas as pd
import numpy as np

# Dataset de Ventas
ventas_data = {
    'VentaID': [1, 2, 3, 4, 5],
    'ProductoID': [101, 102, 103, 104, 101],
    'ClienteID': [1001, 1002, 1003, 1004, 1001],
    'Fecha': ['2021-01-01', '2021-01-02', '2021-01-02', '2021-01-03', '2021-01-04'],
    'Cantidad': [2, 1, 2, 1, 3],
    'Precio': [22.5, 45.0, 19.5, 10.0, 22.5]
}
ventas_df = pd.DataFrame(ventas_data)

# Dataset de Productos
productos_data = {
    'ProductoID': [101, 102, 103, 104],
    'NombreProducto': ['Producto A', 'Producto B', 'Producto C', 'Producto D'],
    'Categoria': ['Electrónica', 'Hogar', 'Juguetes', 'Libros'],
    'PrecioUnitario': [22.5, 45.0, 19.5, 10.0]
}
productos_df = pd.DataFrame(productos_data)

# Dataset de Clientes
clientes_data = {
    'ClienteID': [1001, 1002, 1003, 1004],
    'NombreCliente': ['Cliente A', 'Cliente B', 'Cliente C', 'Cliente D'],
    'Region': ['Norte', 'Sur', 'Este', 'Oeste'],
    'Segmento': ['Corporativo', 'Individual', 'Individual', 'Corporativo']
}
clientes_df = pd.DataFrame(clientes_data)

# --- Paso 1: Combinación de Datasets ---
# Unir ventas con productos basado en 'ProductoID'
ventas_productos_df = pd.merge(ventas_df, productos_df, on='ProductoID')

# Unir el resultado anterior con clientes basado en 'ClienteID'
ventas_completa_df = pd.merge(ventas_productos_df, clientes_df, on='ClienteID')

# --- Paso 2: Enriquecimiento del Dataset ---
# Añadir una columna de margen de ganancia (Precio - PrecioUnitario)
ventas_completa_df['MargenGanancia'] = ventas_completa_df['Precio'] - ventas_completa_df['PrecioUnitario']

# --- Paso 3: Reorganización para Análisis Específico ---
# Pivotar las ventas por Producto y Categoría a lo largo del tiempo
pivot_df = ventas_completa_df.pivot_table(values='Cantidad', index=['NombreProducto', 'Categoria'], columns='Fecha', aggfunc='sum')

# Crosstab para analizar la relación entre segmento de clientes y categorías de productos
crosstab_df = pd.crosstab(ventas_completa_df['Segmento'], ventas_completa_df['Categoria'])

# --- Paso 4: Análisis Preliminar ---
# Resumen estadístico del DataFrame completo
analisis_estadistico = ventas_completa_df.describe()

# Mostrar DataFrames resultantes
print("Ventas completa combinada:\n", ventas_completa_df)
print("\nPivot Table (Cantidad vendida por producto y categoría a lo largo del tiempo):\n", pivot_df)
print("\nCrosstab (Segmento de clientes vs Categoría de productos):\n", crosstab_df)
print("\nAnálisis Estadístico:\n", analisis_estadistico)
