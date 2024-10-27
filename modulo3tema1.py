
#ejercicio 1
import pandas as pd
# Creación de un simple DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'], 'Age': [28, 34, 29, 32]}
df = pd.DataFrame(data)
print(df)

#Ejercicios entregables
#ejercicio 2
#tras haber importado pandas y crear un dataframe ahora creo un dataFrame como se me pide en el ejercicio para que me devuelva la lista de nombres y edad
codedata = {'Nombre': ['Carlos', 'Marta', 'Pedro', 'Elena'], 'Edad': [25, 30, 22, 28]}
df_personas = pd.DataFrame(codedata)
print(df_personas)

#ejercicio 3: selecciono la primera columna con los valores y la primera fila
print(df_personas['Nombre'])
print(df_personas.iloc[0])

#ejercicio 4: hago un filtrado de los que superan 27 años
print(df_personas[df_personas['Edad'] > 27])






