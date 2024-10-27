#defino una superclase
class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre
#defino una subclase con un atributo más (nombre del dueño)
class Mascota(Animal):
    def __init__(self, especie, nombre, nombre_del_dueño):
#le digo que la subclase hereda especie y nombre de la superclase y que nombre del dueño es atributo propio
        super().__init__(especie, nombre)
        self.nombre_del_dueño = nombre_del_dueño
#le pido imprimir datos (los 3 atributos)
    def imprime_datos(self):
        print(f'Especie: {self.especie}, Nombre: {self.nombre}, Nombre del dueño: {self.nombre_del_dueño}')
#creo instancia de mascota con tres datos y le pido imprimir datos
mi_mascota = Mascota('Perro', 'Firulais', 'Juan Pérez')
mi_mascota.imprime_datos()