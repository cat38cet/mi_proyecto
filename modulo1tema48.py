#importo re
import re
#escribo el texto
texto = "Los marineros zarpan al amanecer para explorar y navegar."
#el patrón es
patron = r"ar\b" 
#realizo la búsqueda e imprimo el resultado de palabras terminadas en -ar
resultado_findall = re.findall(patron, texto)
print("palabras que terminan en 'ar:' ", resultado_findall)
# Uso de split para dividir el string y divido por espacios
resultado_split = re.split(r" ", texto)
print("División del string en palabras:", resultado_split)
# Uso de sub para reemplazar palabras
resultado_sub = re.sub(r"marineros", "viajeros", texto)  # Reemplazar "marineros" por "viajeros"
print("String después de reemplazar palabras:", resultado_sub)