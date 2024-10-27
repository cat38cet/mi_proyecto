import math

# Defino una función lambda para calcular el perímetro de un círculo
perimetro_circulo = lambda radio: math.pi * radio *radio

# Uso la función lambda para calcular el perímetro con un radio de 5
resultado = perimetro_circulo(5)

# Imprime el resultado
print(resultado)