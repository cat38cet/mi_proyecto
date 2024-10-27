# Manejo de una variable no declarada
try:
    print(variable_no_declarada)
except NameError:
    print("Error: La variable no está definida.")

# División por cero
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")   

# Acceso a un índice inexistente en una lista
try:
    lista = [1, 2, 3]
    print(lista[5])
except IndexError:
    print("Error: El índice no existe en la lista.")

# Conversión de tipo fallida
try:
    numero = int("abc")
except ValueError:
    print("Error: No se puede convertir la cadena en un número.")

# Abro un archivo inexistente
try:
    archivo = open("archivo_inexistente.txt", "r")
except FileNotFoundError:
    print("Error: El archivo no fue encontrado.")