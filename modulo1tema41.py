#defino la superclase vehículo y los 2 atributos 
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def imprime_datos(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')
#defino la subclase vehículo eléctrico y lo dejo vacío
class VehiculoElectrico(Vehiculo):
    pass
#creo una instancia de mi vehículo
mi_vehiculo = Vehiculo('Toyota', 'Corolla')
mi_vehiculo.imprime_datos()
#creo una instancia de mi vehículo eléctrico
mi_vehiculo_electrico = VehiculoElectrico('Tesla', 'Model S')
mi_vehiculo_electrico.imprime_datos()
#extiendo la clase de vehículo eléctrico con autonomía
class VehiculoElectrico(Vehiculo):
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)
        self.autonomia = autonomia

    def imprime_autonomia(self):
        print(f'Autonomía: {self.autonomia} km')
#creo una nueva instancia de vehiculo electrico 2 con el nuevo atributo
mi_vehiculo_electrico2 = VehiculoElectrico('Nissan', 'Leaf', 300)
#llamo a los metodos para imprimir los atributos datos y autonomía
mi_vehiculo_electrico2.imprime_datos()
mi_vehiculo_electrico2.imprime_autonomia()
  