"""17. Crear una lista con los 10 primeros números al cuadrado y mostrar el resultado en
terminal."""

lista = []

for i in range(1, 11):
    k = i ** 2
    lista.append(k)

print("Los 10 primeros números al cuadrado son: {}".format(lista))