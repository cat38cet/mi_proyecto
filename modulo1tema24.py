#creo la variable entrada donde pido que me devuelva un valor en texto
#no pongo int antes de input pq son palabras
entrada = input("introduce el nombre de un color:\n")
#creo la variable colores con la lista de colores
colores = ["rojo", "verde", "azul", "rosa"]
#creo la condición de que imprima si algún color está en la lista pues que imprima la entrada
if entrada in colores:
    print("el color que buscas está admitido")
#de lo contrario imprime otro texto
else:
    print("color no admitido")