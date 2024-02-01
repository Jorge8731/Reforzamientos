"""7. Borra el primer ítem de la lista usando debidamente su índice."""

lista = ['cálculo', 'física', 'química', 'redacción', 'muestreo', "física"]

lista.append("matemática")
lista.append("redacción")
lista.append("cálculo")
lista.append("cálculo")


print("La lista de ítems es: {}".format(lista))

del lista[0]

print("La lista de ítems actualizada es: {}".format(lista))