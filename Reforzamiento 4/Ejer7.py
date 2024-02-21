"""7. Creando un archivo principal (Ejer5.py) donde importará a un módulo
(operaciones.py) el cuál contendrá las siguientes funciones:

- Una función que genere 30 números enteros aleatorios entre 0 y
100, que muestre en pantalla esta lista.
- Otra función que ordene los valores de una lista y volver a
mostrarla."""

from func import operaciones2

numeros_generados = operaciones2.generar_numeros()

lista_ordenada = operaciones2.ordenar_lista(numeros_generados)
