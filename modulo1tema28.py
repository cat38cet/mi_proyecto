#creo una variable a la que le doy valor
x = 0
#creo un bucle con condicional que indica cuando se rompre el bucle
while x < 30:
    if x == 15:
        print("Se rompió la ejecución del bucle cuando x valía:", x)
        break
#creo otro bucle con condicional que indica cuando se rompe el bucle    
    if x == 4 or x == 6 or x == 10:
        print("Se saltó el valor:", x)
        x += 1
#hacemos saltos del bucle con continue
        continue
    print("El valor del bucle es:", x)
    x += 1