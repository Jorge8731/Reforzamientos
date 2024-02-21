def pedir_valores():
    while True:
        try:
            num1 = int(input("Ingrese el primer número entero: "))
            num2 = int(input("Ingrese el segundo número entero: "))
            return num1, num2
        except ValueError:
            print("El valor no es válido. Ingrese otro.")


def sumar(num1, num2):
    return num1 + num2
