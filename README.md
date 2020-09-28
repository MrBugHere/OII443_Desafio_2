# OII443_Desafio_2

integrantes: Leonardo Durán, José García, Tomás Rojas

para ejecuatar este programa se debe tener instalado python 3, luego para su ejecucion escribir en terminal "python controlador.py"

#Solucion 
Para la solucion del problema se modeló la clase estado, el cual tiene como atributo: tablero, knight_enemigo , knight_enemigo_pos, knight_aliado, knight_aliado_pos, estos atributos son importados desde el archivo json "tablero.json" y esta representa el estado inicial. Luego para determinar el movimiento de un caballo se crea la clase accion para guardar los datos del tipo de movimiento y la id del caballo. Cada moviemiento representa cada una da las 8 posibilidades que tiene el caballo para moverse, teniendo un arreglo de 0 hasta 7 y se determina en la funcion getActions(). Y luego se ocupa la funcion transition() para generar los estados con las acciones obtenidas.

Para determinar el mejor movimiento se utiliza el algoritmo de Monte carlo tree search, el cual haciendo simulaciones determina el mejor movimiento. Para esto se utilizaron nodos que poseen estados y otra información importante, como un valor UCT propio. El arbol se va construyendo con nodos teniendo una lista de hijos. En el proceso de MCTS primero se selecciona el nodo con mayor valor UCT (decidimos ponerle φ (1.6180...) a el nivel de Confianza), de poseer hijos para expander se expande un nuevo hijo, y luego se simula. En la simulación (default policy) se juega una partida totalmente aleatoria y retorna si tuvo una victoria o no. Una vez se consigue el resultado de la simulación se pasa a una fase de feedback, primero se actualiza el nodo actual y sus hijos con la cantidad de victorias y simulaciones (+1 a las simulaciones y lo mismo si hubo victoria, sino no se suma nada a las victorias), y por último se actualiza el valor UCT de todos los nodos. Luego se repite hasta que se acabe el tiempo, una vez termine ese tiempo va a elegir de los hijos del nodo raíz el nodo con la mayor cantidad de simulaciones (ya que ese es el que fue consistentemente más prometedor).

Por último se retorna la acción a ser jugada para el controlador.
