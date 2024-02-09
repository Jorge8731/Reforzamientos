"""2. Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la
función una vez y mostrar el resultado por consola). Los números
serán ingresados y solicitados al usuario."""

def cuadrados(n1, n2):
    lista = []
    for n in range(n1, n2 + 1):
        lista.append(n ** 2)
    return lista

print(cuadrados(6, 10))

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

print("Los cuadrados que hay entre los números es: {}".format(cuadrados(n1, n2)))