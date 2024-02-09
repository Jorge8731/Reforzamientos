"""10. Crear una clase llamada Alumno que tenga como atributos el nombre,
edad y la nota final del alumno. Crear los métodos para inicializar sus
atributos, otro para imprimirlos y un método para mostrar un mensaje
con el resultado de la nota y si ha aprobado (mayor o igual a 11) o no"""

class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir_datos(self):
        print("Nombre del alumno: ", self.nombre)
        print("Edad del alumno: ", self.edad)
        print("Nota final del alumno: ", self.nota_final)

    def resultado(self):
        if self.nota_final >= 11:
            print(f"El alumno está aprobado con {self.nota_final}.")
        else:
            print(f"El alumno está desaprobado con {self.nota_final}.")

alumno1 = Alumno("Jorge", 19, 20)
alumno1.imprimir_datos()
alumno1.resultado()