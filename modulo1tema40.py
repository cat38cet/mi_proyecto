#declarar clases vacías con pass y eliminar objetos
#defino la clase vacía con pass
class Vehiculo:
    pass
#creo una instancia con un objeto (vehículo) y añado dos atributos (tipo y modelo) e imprimo
mi_vehiculo = Vehiculo()
mi_vehiculo.tipo = 'Automóvil'
mi_vehiculo.modelo = 'Mustang'
print(mi_vehiculo.tipo, mi_vehiculo.modelo)
#elimino el atributo modelo con del
del mi_vehiculo.modelo
#intento imprimir modelo y da error e indico con except la frase que debe devolver
try:
    print(mi_vehiculo.modelo)
except AttributeError:
    print("El atributo 'modelo' ha sido eliminado.")
#elimino el objeto
del mi_vehiculo y uso try para imprimir y except para que devuelva el texto una vez que de error
    try:
    print(mi_vehiculo)
except NameError:
    print("El objeto 'mi_vehiculo' ha sido eliminado.")