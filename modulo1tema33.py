#indico los dos diccionarios
teclado1 = { 'Categoría': 'Teclados', 'Modelo': 'HyperX Alloy FPS Pro', 'Precio': '89,99'} 

teclado2 = { 'Categoría': 'Teclados', 'Modelo': 'Corsair K55 RGB', 'Precio': '59,99'}
#elimino teclado1
del teclado1
#elimino categoría y precio de teclado2. Después imprimo y solo devuelve el modelo
del teclado2['Categoría']
del teclado2['Precio']
print(teclado2)