"""2. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
lista = [2, 6, 10, 4, 5, 23, 1]
lista[10]"""


def elemento_lista():
    lista = [2, 6, 10, 4, 5, 23, 1]
    try:
        elemen = lista[10]
        return elemen
    except IndexError as error:
        print("Error: El índice está fuera del rango de la lista.")
        print("Causa: " + str(error))
        print("Solución: Utilice un índice que esté en la lista.")


elemento_lista()
