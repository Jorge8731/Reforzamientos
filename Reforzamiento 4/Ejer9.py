"""9. Crear una función que pida al usuario un número entero entre 1 y 20 y
guarde en un fichero (que no existe) con el nombre tabla.txt la tabla
de multiplicar de ese número, done n es el número introducido."""


def generar_tabla():
    try:
        numero = int(input("Ingrese un número entre el 1 y 20: "))

        if numero >= 1 and numero <= 20:
            tabla = [f"{numero} x {i} = {numero * i}\n" for i in range(1, 11)]

            file = open("my_files/tabla.txt", "w")
            file.writelines(tabla)
            file.close()

            print("Tabla generada correctamente.")
        else:
            print("El número ingresado está fuera del rango.")

    except ValueError:
        print("El valor ingresado no es válido. Ingrese otro.")


generar_tabla()
