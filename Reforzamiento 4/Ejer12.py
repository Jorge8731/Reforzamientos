"""12. Crear una función decoradora que dará los buenos días antes de
ejecutar una función a ser decorada y luego de ser ejecutada lanzará
un mensaje diciendo “Hasta luego”.
La función a decorar pedirá el nombre de una persona y retornará el
mensaje “Soy ‘nombre’”."""


def funcionA(funcionB):
    def funcionC():
        print("Buenos días!")
        nombre = input("Ingrese su nombre: ")
        mensaje = funcionB(nombre)
        print(mensaje)
        print("Hasta luego")
        return mensaje
    return funcionC


@funcionA
def funcion_a_decorar(nombre):
    return "Soy {}".format(nombre)


mensaje = funcion_a_decorar()
