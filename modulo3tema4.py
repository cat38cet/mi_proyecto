#Parte 1: Preguntas
#¿Qué es un DataFrame en el contexto de la biblioteca Pandas?
#Un DataFrame es una estructura de datos con 2 dimensiones. Es parecido a una tabla en bases de datos o una hoja de cálculo en Excel. Se forma de filas y columnas, donde cada columna puede tener un tipo de dato diferente.

#Describe la estructura básica de un DataFrame.
#Un DataFrame tiene una estructura de datos semejante a la de una tabla, con etiquetas para las filas (índice) y las columnas. Cada columna representa una serie de datos y puede tener un tipo de dato distinto.

#¿Qué son los índices en un DataFrame y cómo se utilizan?
#Los índices son las etiquetas de las filas de un DataFrame. Los utilizamos para acceder además de identificar los datos de las filas de manera eficiente. Los índices se pueden personalizar y automatizar.

#Explica cómo seleccionarías una columna específica en un DataFrame.
#Para seleccionar una columna específica en un DataFrame, se usa notación de corchetes df['columna'] o acceder mediante atributos df.columna si no hay espacios o caracteres especiales en el nombre.

#Menciona al menos dos métodos para crear un DataFrame.

#A partir de un diccionario: df = pd.DataFrame(diccionario)
#A partir de listas: df = pd.DataFrame(lista_de_listas, columns=columnas)
#¿Qué ventajas tiene el uso de DataFrames sobre las estructuras de datos tradicionales como listas y diccionarios?
#Los DataFrames permiten una manipulación más eficiente de datos tabulares, permiten operaciones vectorizadas (más rápidas). Se pueden usar distintos tipos de datos por columna, y ofrecen muchas funciones para análisis de datos, como filtrado y agregación.

#¿Cómo se puede modificar el índice de un DataFrame existente?
#Usando el método .set_index() para cambiar el índice a una columna existente o .reset_index() para restaurar el índice numérico predeterminado.

#Nombra una función que permita calcular estadísticas básicas de las columnas numéricas de un DataFrame.
#La función .describe() proporciona un resumen estadístico de las columnas numéricas.

#Parte 2: 
import pandas as pd

# 1. Creación del DataFrame
codedata = {
    'Nombre': ['Ana', 'Jorge', 'Marta', 'Pedro', 'Lucía'],
    'Edad': [23, 21, 22, 25, 24],
    'Carrera': ['Ingeniería', 'Matemáticas', 'Física', 'Arte', 'Derecho'],
    'Correo': [
        'ana@universidad.edu', 'jorge@universidad.edu', 'marta@universidad.edu',
        'pedro@universidad.edu', 'lucia@universidad.edu'
    ]
}

estudiantes = pd.DataFrame(codedata)
print(estudiantes)

#2. Acceso a los datos
# Selecciono y muestro la columna 'Carrera'
print("Columna Carrera:")
print(estudiantes['Carrera'])

# Filtro y muestro los estudiantes mayores de 22 años
print("\nEstudiantes mayores de 22 años:")
print(estudiantes[estudiantes['Edad'] > 22])

#3. Manipulación de datos
# Añado la columna 'Graduado' con valores booleanos
estudiantes['Graduado'] = [True, False, False, True, True]

# Crear la nueva fila
nueva_fila = pd.DataFrame({
    'Nombre': ['MiNombre'], 
    'Edad': [28], 
    'Carrera': ['IA'], 
    'Correo': ['miemail@universidad.edu'], 
    'Graduado': [True]
})

# Añado la fila usando pd.concat()
estudiantes = pd.concat([estudiantes, nueva_fila], ignore_index=True)
print(estudiantes)

#4. Exportación de datos
# Exportar a archivo CSV
estudiantes.to_csv('estudiantes.csv', index=False)

