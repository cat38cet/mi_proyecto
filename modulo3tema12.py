import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generar un dataset simulado de ventas diarias
np.random.seed(0)
fechas = pd.date_range(start='2021-01-01', periods=10000, freq='h')  # Cambia 'H' por 'h'
ventas_diarias = np.random.randint(100, 200, size=len(fechas))

# Crear DataFrame
df_ventas = pd.DataFrame({'Fecha': fechas, 'Ventas': ventas_diarias})
df_ventas.set_index('Fecha', inplace=True)

# 1. Exploración Inicial
print("Primeras entradas del dataset:")
print(df_ventas.head())
print("\nÚltimas entradas del dataset:")
print(df_ventas.tail())

# 2. Resampling de Datos: Agrupar ventas diarias en ventas mensuales
ventas_mensuales = df_ventas.resample('M').sum()  # Sumar las ventas por mes
print("\nVentas mensuales:")
print(ventas_mensuales)

# 3. Cálculo de Estadísticas Móviles
df_ventas['Promedio_Movil_7'] = df_ventas['Ventas'].rolling(window=7).mean()  # Promedio móvil de 7 días
df_ventas['Promedio_Movil_30'] = df_ventas['Ventas'].rolling(window=30).mean()  # Promedio móvil de 30 días

# 4. Visualización de Resultados
plt.figure(figsize=(14, 8))

# Ventas diarias
plt.subplot(3, 1, 1)
plt.plot(df_ventas.index, df_ventas['Ventas'], label='Ventas Diarias', color='blue')
plt.title('Ventas Diarias')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.legend()

# Ventas mensuales
plt.subplot(3, 1, 2)
plt.plot(ventas_mensuales.index, ventas_mensuales['Ventas'], label='Ventas Mensuales', color='orange')
plt.title('Ventas Mensuales')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.legend()

# Estadísticas móviles
plt.subplot(3, 1, 3)
plt.plot(df_ventas.index, df_ventas['Promedio_Movil_7'], label='Promedio Móvil 7 días', color='green')
plt.plot(df_ventas.index, df_ventas['Promedio_Movil_30'], label='Promedio Móvil 30 días', color='red')
plt.title('Promedios Móviles')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.legend()

plt.tight_layout()
plt.show()

