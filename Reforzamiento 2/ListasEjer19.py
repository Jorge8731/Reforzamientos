"""19. Crea una lista vacía (con 10 posiciones), pedir al usuario c/u sus valores y que
finalmente se devuelva la suma y la media de los números ingresados de la lista."""

lista = []

for i in range(10):
    valor = float(input(f"Ingresa el valor {i + 1}: "))
    lista.append(valor)

suma = sum(lista)
media = suma / len(lista)

print("La suma de los valores es: {}".format(suma))
print("La media de los valores es: {}".format(media))