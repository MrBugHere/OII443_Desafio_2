# OII443_Desafio_2

integrantes: Leonardo Durán jose, Jose Garcia, Tomas Rojas

para ejecuatar este programa se debe tener instalado python 3, luego para su ejecucion escribir en terminal "python controlador.py"

#Solucion 
Para la solucion del problema se modelo la clase estado, el cual tiene como atributo: tablero, knight_enemigo , knight_enemigo_pos, knight_aliado, knight_aliado_pos, estos atributos son importados desde el archivo json "tablero.json" y esta reprersenta el estado inicial. Luego para determinar el movimiento de un caballo se crea la clase accion para guardar los datos del tipo de movimiento y la id del caballo. Cada moviemiento representa cada una da las 8 posibilidades que tiene el caballo para moverse, teniendo un arreglo de 0 hasta 7 y se determina en la funcion getActions(). Y luego se ocupa la funcion transition() para generar los estados con las acciones obtenidas.

Para determinar el mejor movimiento se utiliza el algoritmo de Montecarlo, el cual haciendo simulaciones determina el mejor movimiento.
