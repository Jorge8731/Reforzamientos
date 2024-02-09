"""1. Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los
números cuya sumatoria de dígitos es menor que 10. Utilizar una o
más funciones, según sea conveniente."""

def sumatoria_digitos(var):
    suma = 0
    while var > 0:
        suma += var % 10
        var = int(var / 10)
    return suma

var_1 = int(input("Ingrese el primer número: "))
var_2 = int(input("Ingrese el segundo número: "))

suma_digitos_var_1 = sumatoria_digitos(var_1)
suma_digitos_var_2 = sumatoria_digitos(var_2)

print(f"La sumatoria de dígitos del primer número es: {suma_digitos_var_1}")
print(f"La sumatoria de dígitos del segundo número es: {suma_digitos_var_2}")

if suma_digitos_var_1 > suma_digitos_var_2:
    print(f"El número con la mayor sumatoria de dígitos es: {var_1}")
elif suma_digitos_var_2 > suma_digitos_var_1:
    print(f"El número con la mayor sumatoria de dígitos es: {var_2}")
else:
    print("Los dos números tienen la misma sumatoria de dígitos.")

if suma_digitos_var_1 < 10:
    print("El primer número tiene una sumatoria de dígitos menor que 10")
if suma_digitos_var_2 < 10:
    print("El segundo número tiene una sumatoria de dígitos menor que 10")