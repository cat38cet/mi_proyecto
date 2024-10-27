#método __init__
#defino la clase coche y con _init_ indico los atributos
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
#creo la función del texto que se solicitará e imprimo
    def describe_coche(self):
        print(f"El coche es un {self.marca} {self.modelo} del año {self.año}.")
#indico los dos tipos de clase que se piden 
coche1 = Coche('Toyota', 'Corolla', 2020)
coche2 = Coche('Honda', 'Civic', 2018)
coche1.describe_coche()
coche2.describe_coche()