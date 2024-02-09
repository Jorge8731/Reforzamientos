"""8. Crear una clase que contenga dos métodos, uno que pida ingresar un
nombre y apellido, un método para pedir su edad y otro método que lo
imprima ambos resultados, pero estarán contenidos en un diccionario.
Comprobar ambos métodos instanciado la clase respectivamente.
Considerar en el constructor los valores necesarios."""

class Persona:
    def __init__(self):
        self.datos = {}

    def ingre_datos(self):
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        self.datos['nombre'] = nombre
        self.datos['apellido'] = apellido

    def ingre_edad(self):
        edad = int(input("Ingrese su edad: "))
        self.datos['edad'] = edad

    def imprimir_datos(self):
        print("Los datos de la persona son:")
        for key, value in self.datos.items():
            print(f"{key}: {value}")

persona = Persona()
persona.ingre_datos()
persona.ingre_edad()
persona.imprimir_datos()