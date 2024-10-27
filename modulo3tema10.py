import pandas as pd
import numpy as np

# Simular la carga de un gran dataset
data = {
    'VentaID': np.arange(1, 10001),
    'ProductoID': np.random.choice([101, 102, 103, 104], 10000),
    'ClienteID': np.random.choice([1001, 1002, 1003, 1004], 10000),
    'Fecha': pd.date_range(start='2021-01-01', periods=10000, freq='H'),
    'Cantidad': np.random.randint(1, 5, size=10000),
    'Precio': np.random.uniform(10, 50, size=10000)
}
df = pd.DataFrame(data)

# Convertir columnas a tipo categórico para ahorrar memoria
df['ProductoID'] = df['ProductoID'].astype('category')
df['ClienteID'] = df['ClienteID'].astype('category')

# Filtrar datos para un producto específico utilizando operaciones vectorizadas
df_filtrado = df[df['ProductoID'] == 102]

# Calcular el total de ventas por cliente utilizando groupby
df_total_ventas = df_filtrado.groupby('ClienteID').apply(lambda x: (x['Cantidad'] * x['Precio']).sum()).reset_index()
df_total_ventas.columns = ['ClienteID', 'TotalVentas']

# Calcular el promedio de precio de venta por producto usando groupby y mean
df_promedio_precios = df.groupby('ProductoID')['Precio'].mean().reset_index()
df_promedio_precios.columns = ['ProductoID', 'PrecioPromedio']

# Mostrar los resultados
print(df_total_ventas.head())
print(df_promedio_precios.head())


# Comparar tiempo de ejecución
import time

start_time = time.time()

# Ejecutar el código original o optimizado

end_time = time.time()
print(f"Tiempo de ejecución: {end_time - start_time} segundos")

# Comparar uso de memoria
from memory_profiler import memory_usage
mem_usage = memory_usage((funcion_a_medirse, (), {}))
print(f"Uso de memoria: {mem_usage} MB")
