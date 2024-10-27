#**kwargs, se usa para diccionarios (que tiene dos partes, claves y valores)
#defino una función  que acepta kwargs
def describir_persona(**kwargs):
#le indico la clave y valor a iterar e imprimo con f y llaves para indicar clave y valor
    for clave, valor in kwargs.items():
        if clave in ['nombre', 'edad', 'profesión']:
            print(f"{clave}: {valor}")
        else:
            print(f"Clave {clave} no reconocida.")
#indico la función y los argumentos de claves y valores
describir_persona(nombre='Ana', edad=32, profesión='Ingeniera', altura='170cm')