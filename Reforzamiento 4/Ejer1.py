"""1. Crear una función para encontrar el error en el siguiente bloque de
código. Crea una excepción para evitar que tu programa se bloquee y
además imprime un mensaje al usuario la causa y/o solución:
suma = 80 + “Hola Pythonista”"""


def suma():
    try:
        sum = 80 + "Hola Pythonista"
        return sum
    except TypeError as error:
        print("Error: No se puede sumar un int con un cadena.")
        print("Causa: " + str(error))
        print("Solución: Sume datos con igual tipo de valor.")


suma()
