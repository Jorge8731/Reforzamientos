"""8.Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con
una lista vacía y otra con una lista no vacía."""

lista_1 = []
lista_2 = ["Hola mundo", 340, 25.17]

def verificar_lista(lista):
    if not lista:
        print("La lista está vacía.")
    else:
        print("La lista no está vacía.")

verificar_lista(lista_1)

verificar_lista(lista_2)