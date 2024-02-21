import random


def generar_numeros():
    numeros_ale = [random.randint(0,100) for i in range(30)]
    print("Lista de números aleatorios:")
    print(numeros_ale)
    return numeros_ale


def ordenar_lista(lista):
    lista_ord = sorted(lista)
    print("Lista ordenada:")
    print(lista_ord)
    return lista_ord
