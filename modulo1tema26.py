#tips para condicionales...if bla_bla= True...if bla:...else:
#se hace con variables boleanas (dos posibles valores...true o false)
#creo la variable verdadera
es_cliente_premium = True
#solicito imprimir un texto si se cumple una condición
if es_cliente_premium:
    print("es cliente premium")
#indico otro texto si se cumple la condición contraria
else:
    print("no es cliente premium")

#creo otro texto al que le indico True y vuelvo a crear una condición y en caso contrario
tiene_compras_altas = True
if tiene_compras_altas:
    print("tiene compras altas")
else:
    print("no tiene compras altas")

#creo otro texto con true y la condición if y el caso contrario elese
es_la_primera_compra = True
if es_la_primera_compra:
    print("es la primera compra")
else:
    print("no es la primera compra")

#creo una condición y el caso contrario
if es_cliente_premium and tiene_compras_altas and es_la_primera_compra:
    print("El cliente es elegible para un descuento.")
else:
    print("El cliente no es elegible para un descuento.")

