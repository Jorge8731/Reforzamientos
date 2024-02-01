"""9.Elevar al exponente de 4 un número que su valor estará asignado a una variable y
luego restar este mismo valor multiplicado por dos (usar pow). Mostrar el resultado en
pantalla."""

var_1 = 7

potencia = pow(var_1, 4)
resta = potencia - (var_1 * 2)

print("El resultado de esta operación es: {}".format(resta))