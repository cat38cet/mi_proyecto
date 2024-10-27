#antes en el tema 17 se ve cómo ordenar elementos de listas con sort() o sorted()
#poner nombredelalista.sort() y lo ordena ascendente de a -z
#si lo quiero descendente se pone reverse=True

#tema 18-contar elementos con len()
#crea una lista q contenga los elementos siguientes
lista=['perro', 'gato', 'conejo', 'pez', 'pájaro']
#imprime cuántos elementos hay en la lista(contar los elementos)
print(len(lista))
#añade dos elementos más a la lista con el método append
lista.append("loro")
lista.append("caballo")
print(lista)
#vuelve a usar el método len para contar la cantidad de elementos de la lista
print(len(lista))
#elimina de la lista el loro, imprime y vuelve a imprimir contando la cantidad que queda
lista.remove("loro")
print(lista)
print(len(lista))
#desafío opcional: crea una función llamada actualizar_lista que reciba una lista y un conjunto de operaciones de elementos.... 
longitud_lista=len(lista)
print(lista)


