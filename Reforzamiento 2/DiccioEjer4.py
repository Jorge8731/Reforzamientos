"""4. Elimina el key edad tipo de tu diccionario, incluyendo su valor.

del var[‘key’]"""

var1 = {"nombre": "Carlos", "edad": 25, "salario": 6000.00}

var1["dni"] = 63484235

print("Mi diccionario es el siguiente: {}".format(var1))

del var1["edad"]

print("Mi diccionario actualizado es el siguiente: {}".format(var1))