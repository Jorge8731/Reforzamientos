"""8. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu diccionario ya creado.
➢ Mostrar en consola los valores de su variable final (ya sea diccionario o lista)."""

diccionario = {"depar1": "Arequipa", "depar2": "Chiclayo", "depar3": "Lima", "depar4": "Trujillo", "depar5": "Junín", "depar6": "Lambayeque"}

carrera = input("Ingresa el nombre de tu carrera: ")

diccionario["carrera"] = carrera

print("Valores del diccionario:")
for key, value in diccionario.items():
    print(f"{key}: {value}")