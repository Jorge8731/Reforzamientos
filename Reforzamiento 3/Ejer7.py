"""7. Crear una clase en python que contenga un método que revierta una
cadena de palabras.
Input: "Hola Pythonista, seguimos adelante"
Output: "adelante seguimos Pythonista Hola"
Llamarlo mínimo 2 veces y mostrar el resultado por consola."""

class Revertir:
    def rever_palabras(self, cadena):
        palabras = cadena.split()
        rever_oracion = ' '.join(reversed(palabras))
        return rever_oracion

revertir = Revertir()

cadena1 = "Hola Pythonista, seguimos adelante"

output1 = revertir.rever_palabras(cadena1)
print(output1)

output2 = revertir.rever_palabras(output1)
print(output2)