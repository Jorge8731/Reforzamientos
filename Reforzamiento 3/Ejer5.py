"""5. Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados
por el usuario también y un segundo parámetro que eliminará de la
lista que fue ingresada a la función, finalmente el output de la función
será la lista actualizada sin el valor que se sacará de la lista. Mostrar
también la lista original y el número que fue eliminado."""

def valores():
    var_1 = input("Ingrese el primer valor: ")
    var_2 = input("Ingrese el segundo valor: ")
    lista = []

    lista.append(var_1)
    lista.append(var_2)

    return lista

def borrar_valor(lista, valor_eliminar):
    print("Lista original:", lista)
    print("Número a eliminar:", valor_eliminar)

    if valor_eliminar in lista:
        lista.remove(valor_eliminar)
        print("Valor eliminado con éxito.")
    else:
        print("El número a eliminar no está en la lista.")

    print("Lista actualizada:", lista)
    return lista

lista_ingresada = valores()
valor_eliminar = input("Ingrese el valor a eliminar de la lista: ")

borrar_valor(lista_ingresada, valor_eliminar)