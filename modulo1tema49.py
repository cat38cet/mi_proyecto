import re
# Texto 
texto = "manzanas, peras, uvas, plátanos, melocotones, naranjas"
busqueda = re.split(",",texto)
print(busqueda)
busqueda = re.sub(",",";",texto)
print(busqueda)
busqueda = re.sub(",",";",texto,2)
print(busqueda)