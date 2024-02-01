"""3. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar el valor
de salario en consola.

var[‘key’] = tuValor"""

var1 = {"nombre": "Carlos", "edad": 25, "salario": 6000.00}

var1["dni"] = 63484235

print("Mi diccionario actualizado es el siguiente: {}".format(var1))

var2 =list(var1)
var1_values = list(var1.values())

print("El valor del salario es: {} soles".format(var1_values[2]))