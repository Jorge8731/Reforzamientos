"""13. Haciendo el uso de *args y **kwargs aplicarlo debidamente para usar
decorar una función que recibirá 4 argumentos los cuales se
multiplicaran entre ellos.
Mensaje previo al usar el decorador “Está por ejecutarse la función” y
mensaje luego de usar el decorador “La función ha sido ejecutado
correctamente”"""


def funcionA(funcionB):
    def funcionC(*args, **kwargs):
        print("Está por ejecutarse la función")
        resultado = funcionB(*args, **kwargs)
        print("El resultado de la multiplicación es:", resultado)
        print("La función ha sido ejecutada correctamente")
        return resultado
    return funcionC


@funcionA
def multiplicacion(*args):
    resultado = 1
    for arg in args:
        resultado *= arg
    return resultado


resultado = multiplicacion(3, 4, 5, 6)
