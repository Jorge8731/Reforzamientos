"""9. Crear una clase llamada círculo que contenga radio en su constructor y
que contenga un método área que devuelva el área de un círculo.
Aplicar excepciones en caso no se ingrese un dato tipo numérico.
Crear adicionalmente un método que devuelva el perímetro del círculo.
Instanciar la clase respectivamente para dos diferentes radios.
Habrá un método donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola."""

class Circulo:
    def __init__(self, radio):
        if not isinstance(radio, (int, float)):
            raise TypeError("El radio debe ser un número")
        self.radio = radio

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio


def crear_circulo():
    radio = input("Ingrese el radio del círculo: ")
    return Circulo(float(radio))


circulo1 = Circulo(5)
circulo2 = Circulo(7)
circulo3 = crear_circulo()

print("Área del círculo 1:", circulo1.area())
print("Perímetro del círculo 1:", circulo1.perimetro())

print("Área del círculo 2:", circulo2.area())
print("Perímetro del círculo 2:", circulo2.perimetro())

print("Área del círculo 3:", circulo3.area())
print("Perímetro del círculo 3:", circulo3.perimetro())