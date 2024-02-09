"""6. Escribir una clase en Python que contenga un método que convierta un
número entero en su cubo y contenga otro método que obtenga el
cuadrado de ese resultado. El valor inicial de resultado deberá estar
creado en el constructor. Considerar un método en la cual le pedirá al
usuario ingresar un valor numérico."""

class Cubo:
    def __init__(self):
        self.resultado = None

    def valor(self):
        var = int(input("Ingrese el número: "))
        self.resultado = var ** 3

    def cuadrado_resul(self):
        return self.resultado ** 2

cubo = Cubo()
cubo.valor()
print("El cuadrado del cubo del número ingresado es:", cubo.cuadrado_resul())