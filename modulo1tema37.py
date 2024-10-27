#EL BUCLE WHILE:creo la clase, le defino lo del tinterior, pongo lo de self, después printeo la función, creo las instancias, y llamo a la función
#creo una clase y defino la función con los atributos como se pide
class Libro:
    def __init__(self, titulo='', autor='', año=0):
        self.titulo = titulo
        self.autor = autor
        self.año = año
#creo la función para describir el libro e imprimo
    def describe_libro(self):
        print(f"El libro '{self.titulo}' fue escrito por {self.autor} en el año {self.año}.")
#creo las instancias de la clase libro
libro1 = Libro('Cien años de soledad', 'Gabriel García Márquez', 1967)
libro2 = Libro('1984', 'George Orwell', 1949)
libro3 = Libro('El principito', 'Antoine de Saint-Exupéry', 1943)
#llamada al método describe_libro para cada instancia
libro1.describe_libro()
libro2.describe_libro()
libro3.describe_libro()