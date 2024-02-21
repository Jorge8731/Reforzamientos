"""14. Crear un decorador donde imprimirá la cantidad de argumentos que
tiene la función a decorar usando *args y **kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es”
mensaje post “La función decoradora terminó de ejecutarse
correctamente”"""


def contador(funcionA):
    def funcionB(*args, **kwargs):
        print("La cantidad de argumentos que tiene la función es:")
        print(len(args) + len(kwargs))
        resultado = funcionA(*args, **kwargs)
        print("La función decoradora terminó de ejecutarse correctamente")
        return resultado
    return funcionB


@contador
def funcion_ejem(*args, **kwargs):
    print("Esta es la función decorada")


funcion_ejem(6, 12, 8, 3, 35, 52)
