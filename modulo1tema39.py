#self
#creo la clase celular y los atributos
class Celular:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprime_especificaciones(self):
        print('Marca:', self.marca)
        print('Modelo:', self.modelo)
#creo una instancia del celular
mi_celular = Celular('Xiaomi', 'Redmi Note 8')
#modifica el modelo del celular
mi_celular.modelo = 'Redmi Note 9'
#imprime las especificaciones del celular
mi_celular.imprime_especificaciones()