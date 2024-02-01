"""3. Quita 2 elementos de tu nueva lista ítems por valor, no por índice."""

lista = ["cálculo", "programación", "física", "química", "marketing", "contabilidad"]

lista.append("redacción")
lista.append("administración")
lista.append("estadística")
lista.append("muestreo")

print("Los valores de mi lista de cursos son: {}".format(lista))

lista.remove("programación")
lista.remove("estadística")

print("Los valores de mi lista de cursos actualizada son: {}".format(lista))