import pandas as pd

# Tarea 7.1: Agrupación y Reestructuración de DataFrames

# Parte 1: Agrupación de Datos
# Creación del DataFrame df_estudiantes
data_estudiantes = {
    'Nombre': ['Ana', 'Luis', 'Marta', 'Juan', 'Laura', 'José'],
    'Sexo': ['F', 'M', 'F', 'M', 'F', 'M'],
    'Edad': [23, 21, 22, 24, 21, 23],
    'Nota Matemáticas': [4.5, 3.8, 4.2, 5.0, 3.5, 4.0],
    'Nota Literatura': [3.5, 4.0, 4.5, 3.8, 4.2, 5.0]
}
df_estudiantes = pd.DataFrame(data_estudiantes)

# Agrupar por 'Sexo' y calcular la media de las notas
media_notas = df_estudiantes.groupby('Sexo')[['Nota Matemáticas', 'Nota Literatura']].mean()
print("Medias de notas por Sexo:")
print(media_notas)

# Parte 2: Filtro y Extracción de Grupos
# Extraer filas de estudiantes masculinos
df_masculinos = df_estudiantes[df_estudiantes['Sexo'] == 'M']
print("\nEstudiantes Masculinos:")
print(df_masculinos)

# Parte 3: Reestructuración de un DataFrame a Formato Largo
df_largo = pd.melt(df_estudiantes, id_vars=['Nombre', 'Edad'], 
                   value_vars=['Nota Matemáticas', 'Nota Literatura'], 
                   var_name='Asignatura', value_name='Nota')
print("\nDataFrame en Formato Largo:")
print(df_largo)

# Parte 4: Reestructuración de un DataFrame a Formato Ancho
df_ancho = df_largo.pivot_table(index=['Nombre', 'Edad'], 
                                 columns='Asignatura', 
                                 values='Nota').reset_index()
# Renombrar columnas
df_ancho.columns.name = None
df_ancho = df_ancho.rename(columns={
    'Nota Matemáticas': 'Nota Matemáticas', 
    'Nota Literatura': 'Nota Literatura'
})
print("\nDataFrame reestructurado en Formato Ancho:")
print(df_ancho)

# Tarea 7.2: Técnicas de Combinación de DataFrames

# Parte 1: Combinar DataFrames con merge
data_empleados = {
    'ID': [1, 2, 3],
    'Nombre': ['Ana', 'Luis', 'Marta'],
    'ID_Departamento': [101, 102, 101]
}
data_departamentos = {
    'ID_Departamento': [101, 102, 103],
    'Nombre_Departamento': ['Ventas', 'Marketing', 'Finanzas']
}
df_empleados = pd.DataFrame(data_empleados)
df_departamentos = pd.DataFrame(data_departamentos)

# Realizar un inner join
resultado_merge = pd.merge(df_empleados, df_departamentos, on='ID_Departamento', how='inner')
print("\nResultado de inner join entre Empleados y Departamentos:")
print(resultado_merge)

# Parte 2: Combinar DataFrames con join
data_empleados_info = {
    'ID': [1, 2, 3],
    'Nombre': ['Ana', 'Luis', 'Marta'],
    'Edad': [23, 21, 22]
}
data_empleados_salario = {
    'ID': [1, 2],
    'Salario': [50000, 55000]
}
df_empleados_info = pd.DataFrame(data_empleados_info)
df_empleados_salario = pd.DataFrame(data_empleados_salario).set_index('ID')

# Realizar un outer join
resultado_join = df_empleados_info.join(df_empleados_salario, on='ID', how='outer')
print("\nResultado de outer join entre Información de Empleados y Salarios:")
print(resultado_join)

# Parte 3: Concatenar DataFrames con concat
data_ventas_2020 = {
    'ID_Venta': [1, 2],
    'Producto': ['A', 'B'],
    'Cantidad': [10, 20]
}
data_ventas_2021 = {
    'ID_Venta': [3, 4],
    'Producto': ['C', 'D'],
    'Cantidad': [15, 25]
}
df_ventas_2020 = pd.DataFrame(data_ventas_2020)
df_ventas_2021 = pd.DataFrame(data_ventas_2021)

# Concatenar los DataFrames
resultado_concat = pd.concat([df_ventas_2020, df_ventas_2021], ignore_index=True)
print("\nDataFrame resultante de la concatenación de Ventas 2020 y 2021:")
print(resultado_concat)
