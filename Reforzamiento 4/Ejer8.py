"""8. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:

- Una función que realizará la carga de un valor entero.
- Una función que mostrará por pantalla la raíz cuadrada de dicho
valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho
número.
- Utilizar el módulo math de python."""

from func import operaciones3

var = operaciones3.pedir_numero()

operaciones3.raiz(var)
operaciones3.potencias(var)
