"""12. Realizar una clase que administre una agenda. Se debe almacenar en
un diccionario dentro de una lista para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:

Añadir contacto
Mostrar contactos
Buscar contacto
(Por DNI)"""

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email, dni):
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email, "dni": dni})

    def mostrar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                print("Nombre:", contacto["nombre"])
                print("Teléfono:", contacto["telefono"])
                print("Email:", contacto["email"])
                print("DNI:", contacto["dni"])

    def buscar_contacto_dni(self, dni):
        encontrado = False
        for contacto in self.contactos:
            if contacto["dni"] == dni:
                print("Contacto encontrado:")
                print("Nombre:", contacto["nombre"])
                print("Teléfono:", contacto["telefono"])
                print("Email:", contacto["email"])
                print("DNI:", contacto["dni"])
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ningún contacto con ese DNI.")

agenda = Agenda()
agenda.agregar_contacto("Jorge", "123456789", "jorge123@gmail.com", "12345678")

print("Mostrando contactos:")
agenda.mostrar_contactos()

print("\nBuscando contacto por DNI:")
agenda.buscar_contacto_dni("12345678")