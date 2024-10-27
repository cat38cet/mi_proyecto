#cómo usar el diccionario con el bucle for (iterar claves y valores con for en un diccionario)
#indico el diccionario teclado1
teclado1 = { 'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '89,99'} 
#pido iterar las claves y los valores con la función for
for clave, valor in teclado1.items():
    print(clave, "=", valor, end=" ")