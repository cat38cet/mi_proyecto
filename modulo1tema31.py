#diccionario es coleccion de objetos con claves y valores
#creo el diccionario con categoría, modelo y precio
teclado2 = { 'Categoría': 'Teclados', 'Modelo': 'Corsair K55 RGB', 'Precio': '59,99'}
#consulto el modelo y el precio
modelo = teclado2 ["Modelo"]
cuesta = teclado2 ["Precio"]
#solicito imprimir el modelo y el precio con una frase que me devuelve
print("el modelo {Modelo} cuesta {Precio}.")


#corregir lo de arriba con esto
#Contenido:
#creo el diccionario con categoría, modelo y precio
teclado2 = { 'Categoría': 'Teclados', 'Modelo': 'Corsair K55 RGB', 'Precio': '59,99'}
#consulto el modelo y el precio
modelo = teclado2 ["Modelo"]
cuesta = teclado2 ["Precio"]
#solicito imprimir el modelo y el precio con una frase que me devuelve
print(f"El modelo {modelo} cuesta {cuesta}.")
 
#Error:
#En la línea de impresión, las llaves {Modelo} y {Precio} están mal definidas porque deberían usar variables en lugar de llaves literales dentro del string.
#Solución:
#print(f"El modelo {Modelo} cuesta {cuesta}.")
#antes tenia puestoesto y estaba mal: cuesta {precio}
