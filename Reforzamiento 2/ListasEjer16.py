"""16. Mostrar sólo los datos comprendidos entre la posición 10 y 35"""

lista = []

for i in range(1, 101):
    lista.append(i)

lista_2 = []

for k in range(lista[9], lista[35]):
    lista_2.append(k)

print("Los valores de la lista entre la posición 10 y 35 son: {}".format(lista_2))