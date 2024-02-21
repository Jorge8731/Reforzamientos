import math


def pedir_numero():
    while True:
        try:
            var = int(input("Ingrese el número: "))
            return var
        except ValueError:
            print("El número no es válido. Pruebe otro.")


def raiz(var):
    raiz_cuadrada = math.sqrt(var)
    print("La raiz cuadrada del número es: {}".format(raiz_cuadrada))


def potencias(var):
    cuadrado = var ** 2
    cubo = var ** 3
    print("El cuadrado del número es: {}".format(cuadrado))
    print("El cubo del número es: {}".format(cubo))
