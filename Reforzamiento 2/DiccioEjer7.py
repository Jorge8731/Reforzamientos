"""7. Crear un diccionario con 6 departamentos en el país.
➢ Borrar cualquier departamento (uno) usando la palabra reservada del.
➢ Comprobar que no existe este departamento borrado dentro del diccionario."""

diccionario = {"depar1": "Arequipa", "depar2": "Chiclayo", "depar3": "Lima", "depar4": "Trujillo", "depar5": "Junín", "depar6": "Lambayeque"}

print("Mi diccionario creado es: {}".format(diccionario))

del diccionario["depar5"]

print("Mi diccionario actualizado es: {}".format(diccionario))