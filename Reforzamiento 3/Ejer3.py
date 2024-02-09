"""3. Crear una función que sume los dígitos del número ingresado y
muestre por consola la suma de estos dígitos."""

def suma_digitos(n):
    suma = 0
    while n > 0:
        suma += n % 10
        n = int(n / 10)
    return suma

n1 = int(input("Ingrese el número: "))

print("La suma de dígitos del número ingresado es: {}".format(suma_digitos(n1)))