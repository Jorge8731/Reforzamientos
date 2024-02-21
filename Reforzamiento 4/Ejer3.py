"""3. Crear una función y dentro la respectiva excepción para el siguiente
bloque de código para que tu programa no se bloquee y además
imprime un mensaje al usuario la causa y/o solución:
persona= { 'nombre':'Xavier', 'apellido':'Rodriguez', 'dni':'63325345'}
persona['profesion']"""


def encontrar_key():
    persona = {'nombre':'Xavier', 'apellido': 'Rodriguez', 'dni': '63325345'}
    try:
        profesion = persona['profesion']
        return profesion
    except KeyError as error:
        print("Error: No existe 'profesion' en el diccionario persona.")
        print("Causa: " + str(error))
        print("Solución: Utilice una clave válida.")


encontrar_key()
