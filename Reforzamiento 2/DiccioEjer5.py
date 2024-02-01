"""5. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos final que tiene."""

var1 = {"nombre": "Carlos", "edad": 25, "salario": 6000.00}

var1["dni"] = 63484235

print("Mi diccionario es el siguiente: {}".format(var1))

var2 =list(var1)
var1_values = list(var1.values())

print("El tipo de dato de nombre es: {}".format(type(var1_values[0])))
print("El tipo de dato de edad es: {}".format(type(var1_values[1])))
print("El tipo de dato de salario es: {}".format(type(var1_values[2])))
print("El tipo de dato de dni es: {}".format(type(var1_values[3])))