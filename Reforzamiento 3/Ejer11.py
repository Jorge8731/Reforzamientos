"""11. Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una
persona. Implementar los métodos necesarios para inicializar los
atributos (constructor), un método para mostrar los datos e indicar si
la persona es mayor de edad o no y otro método que bonificación que
retornará el 20% adicional de su sueldo.
Instanciar por lo menos la clase con 2 diferentes personas."""

class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Sueldo:", self.sueldo)

    def mayor_de_edad(self):
        if self.edad >= 18:
            print("Es mayor de edad.")
        else:
            print("No es mayor de edad.")

    def bonificacion(self):
        return self.sueldo * 0.20 + self.sueldo


# Instanciar la clase con dos personas diferentes
persona1 = Persona("Carlos", 23, 8000)
persona2 = Persona("Alejandra", 17, 5000)

# Mostrar los datos de las personas y si son mayores de edad o no
print("Persona 1:")
persona1.mostrar_datos()
print("Bonificación:", persona1.bonificacion())

print("\nPersona 2:")
persona2.mostrar_datos()
print("Bonificación:", persona2.bonificacion())