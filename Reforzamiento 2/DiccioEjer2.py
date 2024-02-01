"""2. Convierte tu diccionario a una lista y mostrar el tipo de datos final convertido en consola."""

var1 = {"nombre": "Carlos", "edad": 25, "salario": 6000.00}

var2 = list(var1)

print("El diccionario convertido a lista es el siguiente: {}".format(var2))

print("El tipo de datos final convertido es: {}".format(type(var2)))