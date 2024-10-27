import re

# Texto de ejemplo
frase = "El número 42 es considerado por muchos como 'la respuesta a la vida, el universo y todo lo demás'."

# Búsqueda con search
resultado1 = re.search(r"respuesta", frase)
print(f"Resultado de re.search: {resultado1}")

# Todas las ocurrencias con findall
resultado2 = re.findall(r"e", frase)
print(f"La letra 'e' se encuentra {len(resultado2)} veces.")

# Comprobación con match
resultado3 = re.match(r"El", frase)
print(f"Resultado de re.match: {resultado3}")

# Reemplazo con sub
resultado4 = re.sub(r"42", "cuarenta y dos", frase)
print(f"Resultado de re.sub: {resultado4}")