"""9. Sumar las dos listas creadas anteriormente y mostrar el resultado en terminal."""

lista_1 = ['cálculo', 'física', 'química', 'redacción', 'muestreo', "física"]

lista_1.append("matemática")
lista_1.append("redacción")
lista_1.append("cálculo")
lista_1.append("cálculo")

lista_2 = []

lista_2.append(3.14)
lista_2.append(12.62)
lista_2.append(8.81)
lista_2.append(173)
lista_2.append(500)
lista_2.append(82)
lista_2.append("Diamante")
lista_2.append("Verano")
lista_2.append("Juan")

suma_listas = lista_1 + lista_2

print("La suma de las listas es: {}".format(suma_listas))