#El condicional if elif else e input, entrada de datos
#convierto a entero el texto y le pido input para recibir el valor y le pido salto de línea
#pongo int porque son números enteros
edad = int(input('¿Cuál es tu edad?\n'))
#le pido el primer condicional e imprimir
if edad <= 0: 
    print('Nadie puede tener esa edad.')
#le pido nuevos condicionales
elif edad >= 1 and edad <= 18: 
    print('Eres menor de edad.')
elif edad > 18 and edad <= 35: 
    print('Eres mayor de 18 y menor o igual a 35.')
elif edad > 35 and edad <= 100:
    print('Eres mayor de edad.')
elif edad > 100:
    print('Eres mayor de 100.')
#le pido un caso contrario de condicionales anteriores o False
else:
    print('Edad no válida.')
