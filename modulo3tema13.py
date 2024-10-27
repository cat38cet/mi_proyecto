import pandas as pd
import numpy as np
import dask.dataframe as dd
import modin.pandas as mpd
import time

# Generar un dataset sintético de transacciones de ventas
n_rows = 10_000_000  # Número de filas en el dataset

# Crear datos sintéticos
data = {
    'id_transaccion': np.arange(n_rows),
    'producto': np.random.choice(['Producto A', 'Producto B', 'Producto C'], n_rows),
    'cantidad': np.random.randint(1, 10, size=n_rows),
    'precio': np.random.uniform(1.0, 100.0, size=n_rows),
    'fecha': pd.date_range(start='2021-01-01', periods=n_rows, freq='T')
}

# Crear DataFrame con Pandas
print("Creando DataFrame con Pandas...")
start_time = time.time()
df_pandas = pd.DataFrame(data)
pandas_time = time.time() - start_time
print(f"Tiempo de creación con Pandas: {pandas_time:.2f} segundos")

# Análisis con Pandas
print("\nAnálisis con Pandas...")
start_time = time.time()
result_pandas = df_pandas.groupby('producto').agg({'cantidad': 'sum', 'precio': 'mean'})
pandas_analysis_time = time.time() - start_time
print(f"Tiempo de análisis con Pandas: {pandas_analysis_time:.2f} segundos")

# Análisis con Dask
print("\nCreando DataFrame con Dask...")
start_time = time.time()
df_dask = dd.from_pandas(df_pandas, npartitions=4)  # Dividir en particiones
dask_time = time.time() - start_time
print(f"Tiempo de creación con Dask: {dask_time:.2f} segundos")

# Análisis con Dask
print("\nAnálisis con Dask...")
start_time = time.time()
result_dask = df_dask.groupby('producto').agg({'cantidad': 'sum', 'precio': 'mean'}).compute()
dask_analysis_time = time.time() - start_time
print(f"Tiempo de análisis con Dask: {dask_analysis_time:.2f} segundos")

# Análisis con Modin
print("\nCreando DataFrame con Modin...")
start_time = time.time()
df_modin = mpd.DataFrame(data)
modin_time = time.time() - start_time
print(f"Tiempo de creación con Modin: {modin_time:.2f} segundos")

# Análisis con Modin
print("\nAnálisis con Modin...")
start_time = time.time()
result_modin = df_modin.groupby('producto').agg({'cantidad': 'sum', 'precio': 'mean'})
modin_analysis_time = time.time() - start_time
print(f"Tiempo de análisis con Modin: {modin_analysis_time:.2f} segundos")

# Mostrar resultados
print("\nResultados de Pandas:")
print(result_pandas)

print("\nResultados de Dask:")
print(result_dask)

print("\nResultados de Modin:")
print(result_modin)
