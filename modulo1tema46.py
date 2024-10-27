import datetime
#crear la variable ahora
ahora = datetime.datetime.now()
# Formato completo de fecha y ahora
print(f"Formato completo: {ahora.strftime('%c')}")
# Solo la hora con AM o PM
print(f"Hora con AM/PM: {ahora.strftime('%I:%M %p')}")

# Solo la fecha en el formato "DD de Mes de YYYY"
print(f"Fecha: {ahora.strftime('%d de %B de %Y')}")

# Día de la semana, número del día del año y semana del año
print(f"Día de la semana: {ahora.strftime('%A')}")
print(f"Día del año: {ahora.strftime('%j')}")
print(f"Semana del año: {ahora.strftime('%U')}")