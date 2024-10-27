import datetime

# creo una variable
ahora = datetime.datetime.now()
print(ahora)


# Creo una fecha personalizada
fecha_especifica = datetime.datetime(2024, 1, 1, 0, 0)
print(fecha_especifica)

# Calculo la diferencia entre fechas
diferencia = ahora - fecha_especifica

# Imprimo la diferencia
print(diferencia)
