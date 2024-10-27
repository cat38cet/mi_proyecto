import re
# texto a buscar
texto1 = "Python 3.8.5 es la versión actual, pero la versión 2.7.18 fue muy popular"
# buscar las ocurrencias de números de versión
versiones = re.findall(r"\d+\.\d+\.\d+", texto1)
print("Números de versión:", versiones)
#busca los digitos que aparecen en el texto
digitos = re.findall(r"\d", texto1)
print("Dígitos:", digitos)
#texto para buscar palabras que empiecen por "pro"
texto2 = "Bienvenidos al curso de programación con Next-IT!"
# encontrar todas las palabras que empiezan con "pro" y le pongo w* para que coloque la palabra entera
palabras_con_pro = re.findall(r"\bpro\w*", texto2)
print("Palabras que empiezan con 'pro':", palabras_con_pro)
# buscar todas las coincidencias de IT que no estén al principio o al final de una palabra
coincidencias_it = re.findall(r"\BIT\B", texto2)
print("Coincidencias de 'IT' que no están al principio o al final:", coincidencias_it)
#texto 3 para buscar
texto3 = "¡Los sets son útiles! set(), get(), reset() - métodos comunes."
#encontrar palabras que terminen en set
metodos_set = re.findall(r"\w+set\b", texto3)
print("Métodos que terminan con 'set':", metodos_set)
# Utiliza un set para buscar todas las ocurrencias de los paréntesis ()
parentesis = re.findall(r"\(\)", texto3)
print("Ocurrencias de paréntesis ():", parentesis)
# String para buscar códigos de error
texto4 = "Error 404: Not Found. Error 500: Internal Server Error."
# buscar todos los códigos de error (ej: "404")
codigos_error = re.findall(r"\d{3}", texto4)
print("Códigos de error:", codigos_error)
# Utiliza \D para obtener todo el texto que no sean dígitos
texto_sin_digitos = re.findall(r"\D+", texto4)
print("Texto que no son dígitos:", texto_sin_digitos)
# texto para buscar correos electrónicos
texto5 = "Contacto: admin@example.com, ventas@example.com, soporte@nextit.org."
# Encuentra todas las direcciones de correo electrónico
emails = re.findall(r"\b\w+@\w+\.\w+\b", texto5)
print("Correos electrónicos:", emails)
# Utiliza \w para encontrar todas las palabras que contengan al menos un carácter alfanumérico y la barra baja
palabras_alfanumericas = re.findall(r"\w+", texto5)
print("Palabras con al menos un carácter alfanumérico:", palabras_alfanumericas)
