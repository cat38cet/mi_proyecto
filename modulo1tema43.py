#creo la variable global hola 
mensaje = "Hola"
#defino una función local con el nombre que se me pide y la inicializo con una frase
def saludo_local():
#defino la variable local    
    mensaje = "Hola desde una función local"
# defino una funcion anidada 
    def Saludo_anidado():
        print(mensaje)
#llamo a la función anidada y a la función saludo local
saludo_anidado()
saludo_local()
print(mensaje)
