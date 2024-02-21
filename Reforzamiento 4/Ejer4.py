"""4. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
string = "Hello Pythonista"
print(string/0)"""


def operacion():
    string = "Hello Pythonista"
    try:
        resultado = string / 0
        return resultado
    except TypeError as error:
        print("Error: No se puede realizar la operación con el tipo de dato del str.")
        print("Causa: " + str(error))
        print("Solución: Utilice operaciones válidas con el tipo de dato.")


operacion()
