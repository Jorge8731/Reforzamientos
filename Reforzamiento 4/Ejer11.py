"""11. Crear una función que creará el archivo calificaciones.txt que contiene
las calificaciones de un curso.
Escribir un programa que contenga las siguientes funciones:

- Una función que guarde el nombre, 2 notas y el promedio (el
promedio lo calculará la función antes de escribirlo en el fichero)
- Y una función que leerá el fichero anterior y dirá si el alumno X,
aprobó o no, tener en cuenta que si tiene un promedio mayor a día
tendrá un mensaje de “Alumno X, aprobado” de lo contrario “Alumno
X, desaprobado”"""


def guardar_datos():
    try:
        nombre = input("Ingrese el nombre: ")
        nota_1 = float(input("Ingrese la primera nota: "))
        nota_2 = float(input("Ingrese la segunda nota: "))

        promedio = (nota_1 + nota_2) / 2

        file = open("my_files/calificaciones.txt", "a+")
        file.writelines(f"{nombre}, {nota_1}, {nota_2}, {promedio}\n")
        file.close()

        print("Calificaciones guardadas correctamente.")

    except ValueError as error:
        print(f"Error: {error}")


def verificar_aprobado(nombre_a):
    try:
        file = open("my_files/calificaciones.txt", "r")
        for line in file:
            datos = line.strip().split(",")
            nombre = datos[0]
            promedio = float(datos[3])
            if nombre == nombre_a:
                if promedio >= 10.5:
                    print(f"Alumno {nombre}, aprobado.")
                else:
                    print(f"Alumno {nombre}, desaprobado.")
                file.close()
                return
        print(f"No se encontraron calificaciones para el alumno {nombre_a}")
        file.close()
    except FileNotFoundError:
        print("No se encontró el archivo 'calificaciones.txt'.")
    except Exception as error:
        print(f"Error: {error}")


guardar_datos()
verificar_aprobado("Carlos")
