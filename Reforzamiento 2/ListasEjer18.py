"""18. Crear una lista con los 15 primeros números impares, luego agregar 3 números flotantes
repetidos (los cuales son impares dentro del rango indicado y que no sea el último
impar).
- Empezando desde 1 y no 0.
- Agregar un cadena en la posición 3 de la lista.
- Eliminar este valor string de la cadena usando del."""

lista = []

for i in range(1, 30, 2):
    lista.append(i)

lista.append(17.53)
lista.append(17.53)
lista.append(17.53)

lista.insert(2, "Hola Pythonistas")

print("La lista es: {}".format(lista))

del lista[2]

print("La lista actualizada es: {}".format(lista))