"""4. Pedir al usuario que ingrese una oración con un mínimo de 3 palabras
la cual será usada por parámetro para una función que se creará e
indicará cuantas palabras existen dentro de la oración ingresada."""

def contar_palabras(oracion):
    palabras = oracion.split()
    return len(palabras)

oracion_usuario = input("Ingrese una oración (mínimo 3 palabras): ")
numero_palabras = contar_palabras(oracion_usuario)

if len(oracion_usuario.split()) <= 3 and len(oracion_usuario.split()) > 0:
    print("La cantidad de palabras en la oración ingresada es:", numero_palabras)
elif len(oracion_usuario.split()) > 3:
    print("La oración tiene más de 3 palabras. Por favor, ingresa otra oración.")
else:
    print("La oración no tiene ni una palabra. Por favor, ingresa otra oración.")