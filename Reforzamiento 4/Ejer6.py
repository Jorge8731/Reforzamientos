"""6. Creando un archivo principal donde llamará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:

- La primera función cargará una un número entero que pedirá al
usuario que ingrese por consola un valor.
- La segunda función solamente sumará dos valores.
- Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo"""

from func import operaciones

num1, num2 = operaciones.pedir_valores()

suma = operaciones.sumar(num1, num2)

print("La suma de los valores es: {}".format(suma))
