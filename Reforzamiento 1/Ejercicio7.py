"""7.De 3 números asignados (tú los propones) a 3 variables se pide hallar la suma de los
valores de los módulos con 3, 5, y 7 respectivamente, mostrar en pantalla el valor de la
suma."""

var_1 = 16
var_2 = 43
var_3 = 27

modulo_1 = var_1 % 3
modulo_2 = var_2 % 5
modulo_3 = var_3 % 7

suma_modulos = modulo_1 + modulo_2 + modulo_3

print("La suma de los valores de los módulos es: {}".format(suma_modulos))