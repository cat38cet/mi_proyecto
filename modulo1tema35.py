#*arg argumentos arbitrarios(numero ilimitado de usos) se usa en funciones
# los argumentos que se usan en cada llamada son 4,3,1,2

#creo la función colores y los argumentos arbitrarios a los que indico pass (para evitar error)
def colores(*args): 
    pass
#indico 4 bloques de argumentos a los que llamo por medio de la llamada de la función
colores('rojo', 'azul', 'verde', 'amarillo')

colores('lila', 'negro', 'rojo')

colores('rosa')

colores('marrón', 'naranja')

#utilizo argumentos concretos para imprimir una frase y abajo le indico los valores
def colores(*args):
    print("El color", args[0], "es mi favorito.", "El color", args[1], "tampoco está mal.")
colores("azul", "rojo")

#creo otra función de argumentos arbitraios llamada suma y llamo a la suma con 5 números e imprimo
def suma(*args):
    print(sum(args))

suma(1, 2, 3, 4, 5)



