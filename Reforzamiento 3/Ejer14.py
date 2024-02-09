"""14. Crear un módulo y un archivo principal (donde llamará las funciones del
módulo) el módulo tendrá una función para ingresar nombres y
apellidos, una función para pedir el tipo de seguro que tiene y otra
función para indicar si es mayor de edad o no (pedir la edad desde
consola)"""

def ingresar_nombre_apellido():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    return nombre, apellido


def tipo_de_seguro():
    seguro = input("¿Qué tipo de seguro tiene? ")
    return seguro


def mayor_de_edad():
    edad = int(input("Ingrese su edad: "))
    return edad >= 18


def main():
    nombre, apellido = ingresar_nombre_apellido()
    print("Nombre completo:", nombre, apellido)

    tipo_seguro = tipo_de_seguro()
    print("Tipo de seguro:", tipo_seguro)

    if mayor_de_edad():
        print("Es mayor de edad.")
    else:
        print("No es mayor de edad.")


if __name__ == "__main__":
    main()