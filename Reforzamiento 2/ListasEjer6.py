"""6. Devuelve la cantidad de veces que se repite un curso (agregarla previamente a la lista)
dentro de la lista."""

lista = ['cálculo', 'física', 'química', 'redacción', 'muestreo', "física"]

lista.append("matemática")
lista.append("redacción")
lista.append("cálculo")
lista.append("cálculo")


print("La lista actualizada es: {}".format(lista))

print("La cantidad de veces que se repite 'cálculo' es: {}".format(lista.count("cálculo")))
print("La cantidad de veces que se repite 'física' es: {}".format(lista.count("física")))
print("La cantidad de veces que se repite 'química' es: {}".format(lista.count("química")))
print("La cantidad de veces que se repite 'redacción' es: {}".format(lista.count("redacción")))
print("La cantidad de veces que se repite 'muestreo' es: {}".format(lista.count("muestreo")))
print("La cantidad de veces que se repite 'matemática' es: {}".format(lista.count("matemática")))