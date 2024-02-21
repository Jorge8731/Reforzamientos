"""10. Crear una función donde se permitirá guardar el nombre, apellido y
edad de un usuario en un fichero (agenda.txt), cada usuario tiene que
estar guardado en una línea diferente y cada dato de una persona tiene
que estar separados por comas."""


def guardar_usuario_en_agenda():
    try:
        nombre = input("Ingrese el nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")
        edad = int(input("Ingrese la edad del usuario: "))

        datos_usuario = f"{nombre}, {apellido}, {edad}\n"

        file = open("my_files/agenda.txt", "a+")
        file.writelines(datos_usuario)
        file.close()

        print("Usuario guardado en la agenda correctamente.")
    except Exception as error:
        print(f"Error: {error}")


guardar_usuario_en_agenda()
