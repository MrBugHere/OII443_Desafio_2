import json
import math
import random
import time
import sys


# Variables Globales
phi = (1 + 5 ** 0.5) / 2
#

class Accion:
    def __init__(self):
        self.knight_id = 0
        self.knight_movement = 0

    def setKnight_id(self, id):
        self.knight_id = id

    def setKnight_movement(self, mov):
        self.knight_movement = mov

    def getKnight_id(self):
        return self.knight_id

    def getKnight_movement(self):
        return self.knight_movement

    def printAccion(self):
        print('Pieza: ', self.knight_id, 'puede realizar el movimiento: ', self.knight_movement)


class Estado:
    def __init__(self, tablero_nuevo, enemigo, aliado, pos_enemigo, pos_aliado):
        self.tablero = self.iniciar(tablero_nuevo)
        self.knight_enemigo = self.iniciar(enemigo)
        self.knight_enemigo_pos = pos_enemigo
        self.knight_aliado = self.iniciar(aliado)
        self.knight_aliado_pos = pos_aliado

    def iniciar(self, tablero):
        for x in range(8):
            tablero[x] = list(tablero[x])
        return tablero

    def printTablero(self):
        for line in self.tablero:
            print('\t'.join(map(str, line)))

    def printAliado(self):
        print(self.knight_aliado)

    def printKnight_aliado_pos(self):
        print(self.knight_aliado_pos)

    def printEnemigo(self):
        print(self.knight_enemigo)

    def printKnight_enemigo_pos(self):
        print(self.knight_enemigo_pos)

    def getTablero(self):
        return self.tablero

    def getPos_knight_enemigo(self, id):
        return self.knight_enemigo_pos[str(id)]

    def getPos_knight_aliado(self, id):
        return self.knight_aliado_pos[str(id)]

    def getEnemigo(self):
        return self.knight_enemigo

    def getAliado(self):
        return self.knight_aliado

    def esAliado(self, x, y):
        if self.knight_aliado[x][y] is not None:
            return True
        return False

    def insertarKnight_tablero(self, x, y, id):
        if self.tablero[x][y] is not None:
            del self.knight_enemigo_pos[str(self.tablero[x][y])]
            self.knight_enemigo[x][y] = None
            self.tablero[x].pop(y)
        self.tablero[x].insert(y, id)
        self.knight_aliado_pos[str(id)] = [y, x]
        self.knight_aliado[x].insert(y, id)

    def esEnemigo(self, y, x):
        if self.knight_enemigo[x][y] is not None:
            return True
        return False

    def insertarKnight_tablero_Enemigo(self, x, y, id):
        if self.tablero[x][y] is not None:
            del self.knight_aliado_pos[str(self.tablero[x][y])]
            self.knight_aliado[x][y] = None
            self.tablero[x].pop(y)
        self.tablero[y].insert(x, id)
        self.knight_enemigo_pos[str(id)] = [x, y]
        self.knight_enemigo[x].insert(y, id)

    def eliminarKnight_tablero(self, x, y):
        self.tablero[x][y] = None

    def whoWon(self):
        if len(self.knight_aliado_pos) - len(self.knight_enemigo_pos) > 0:
            return 1
        else:
            return 0


def getActions(estado):
    lista_acciones = []
    for i in range(200, 216):
        knight_pos = estado.getPos_knight_aliado(i)
        # print(knight_pos)
        x = knight_pos[0]
        # print (x)
        y = knight_pos[1]
        # print(y)
        directions = [0, 1, 2, 3, 4, 5, 6, 7]
        tablero = estado.getTablero()

        if x + 2 < 8 and y + 1 < 8:
            if estado.esAliado(x + 2, y + 1):
                directions.remove(0)
        else:
            if x + 2 >= 8 or y + 1 >= 8:
                directions.remove(0)

        if x + 1 < 8 and y + 2 < 8:
            if estado.esAliado(x + 1, y + 2):
                directions.remove(1)
        else:
            if x + 1 >= 8 or y + 2 >= 8:
                directions.remove(1)

        if y + 2 < 8 and x - 1 >= 0:
            if estado.esAliado(x - 1, y + 2):
                directions.remove(2)
        else:
            if x - 1 < 0 or y + 2 >= 8:
                directions.remove(2)

        if y + 1 < 8 and x - 2 >= 0:
            if estado.esAliado(x - 2, y + 1):
                directions.remove(3)
        else:
            if x - 2 < 0 or y + 1 >= 8:
                directions.remove(3)

        if y - 1 >= 0 and x - 2 >= 0:
            if estado.esAliado(x - 2, y - 1):
                directions.remove(4)
        else:
            if y - 1 < 0 or x - 2 < 0:
                directions.remove(4)

        if y - 2 >= 0 and x - 1 >= 0:
            if estado.esAliado(x - 1, y - 2):
                directions.remove(5)
        else:
            if x - 1 < 0 or y - 2 < 0:
                directions.remove(5)

        if y - 2 >= 0 and x + 1 < 8:
            if estado.esAliado(x + 1, y - 2):
                directions.remove(6)
        else:
            if x + 1 >= 8 or y -2 < 0:
                directions.remove(6)

        if y - 1 >= 0 and x + 2 < 8:
            if estado.esAliado(x + 2, y - 1):
                directions.remove(7)
        else:
            if y - 1 < 0 or x + 2 >= 8:
                directions.remove(7)

        for direction in directions:
            accion = Accion()
            accion.setKnight_id(i)
            accion.setKnight_movement(direction)
            lista_acciones.append(accion)

    return lista_acciones


def transition(accion, estado):
    nuevo_estado = estado
    knight_pos = estado.getPos_knight_aliado(accion.getKnight_id())
    # print(knight_pos)
    x = knight_pos[0]
    # print (x)
    y = knight_pos[1]

    if accion.getKnight_movement() == 0:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x + 2
        y = y + 1
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())
        print("hola")

    if accion.getKnight_movement() == 1:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x + 1
        y = y + 2
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 2:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x - 1
        y = y + 2
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 3:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x - 2
        y = y + 1
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 4:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x - 2
        y = y - 1
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 5:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x - 1
        y = y - 2
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 6:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x + 1
        y = y - 2
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 7:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x + 2
        y = y - 1
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    return nuevo_estado


def isTerminal(estado):
    if (len(estado.knight_enemigo_pos) == 0) or (len(estado.knight_aliado_pos) == 0):
        return True
    return False


def getActions_Enemigo(estado):
    lista_acciones = []
    for i in range(100, 115):
        knight_pos = estado.getPos_knight_enemigo(i)
        # print(knight_pos)
        x = knight_pos[0]
        # print (x)
        y = knight_pos[1]
        # print(y)
        directions = [0, 1, 2, 3, 4, 5, 6, 7]
        tablero = estado.getTablero()

        if y + 1 < 8 and x + 2 < 8:
            if estado.esEnemigo(y + 1, x + 2):
                directions.remove(0)
        else:
            if x + 2 >= 8 or y + 1 >= 8:
                directions.remove(0)

        if y + 2 < 8 and x + 1 < 8:
            if estado.esEnemigo(y + 2, x + 1):
                directions.remove(1)
        else:
            if x + 1 >= 8 or y + 2 >= 8:
                directions.remove(1)

        if y + 2 < 8 and x - 1 >= 0:
            if estado.esEnemigo(y + 2, x - 1):
                directions.remove(2)
        else:
            if x - 1 < 0 or y + 2 >= 8:
                directions.remove(2)


        if y + 1 < 8 and x - 2 >= 0:
            if estado.esEnemigo(y + 1, x - 2):
                directions.remove(3)
        else:
            if x - 2 < 0 or y + 1 >= 8:
                directions.remove(3)


        if y - 1 >= 0 and x - 2 >= 0:
            if estado.esEnemigo(y - 1, x - 2):
                directions.remove(4)
        else:
            if y - 1 < 0 or x - 2 < 0:
                directions.remove(4)


        if y - 2 >= 0 and x - 1 >= 0:
            if estado.esEnemigo(y - 2, x - 1):
                directions.remove(5)
        else:
            if x - 1 < 0 or y - 2 < 0:
                directions.remove(5)


        if y - 2 >= 0 and x + 1 < 8:
            if estado.esEnemigo(y - 2, x + 1):
                directions.remove(6)
        else:
            if x + 1 >= 8 or y -2 < 0:
                directions.remove(6)


        if y - 1 >= 0 and x + 2 < 8:
            if estado.esEnemigo(y - 1, x + 2):
                directions.remove(7)
        else:
            if y - 1 < 0 or x + 2 >= 8:
                directions.remove(7)


        for direction in directions:
            accion = Accion()
            accion.setKnight_id(i)
            accion.setKnight_movement(direction)
            lista_acciones.append(accion)

    return lista_acciones


def transitionEnemigo(accion, estado):
    nuevo_estado = estado
    knight_pos = estado.getPos_knight_enemigo(accion.getKnight_id())
    # print(knight_pos)
    x = knight_pos[0]
    # print (x)
    y = knight_pos[1]

    if accion.getKnight_movement() == 0:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x + 2
        y = y + 1
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 1:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x + 1
        y = y + 2
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 2:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x - 1
        y = y + 2
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 3:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x - 2
        y = y + 1
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 4:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x - 2
        y = y - 1
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 5:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x - 1
        y = y - 2
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 6:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x + 1
        y = y - 2
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    if accion.getKnight_movement() == 7:
        nuevo_estado.eliminarKnight_tablero(x, y)
        x = x + 2
        y = y - 1
        nuevo_estado.insertarKnight_tablero(x, y, accion.getKnight_id())

    return nuevo_estado


#
# Estructuras Para Implementar Arbol
#

class Node:
    def __init__(self, sInput, pInput, wInput, cInput, vInput, aInput, tInput, uInput):
        self.state = sInput
        self.parent = pInput
        self.childs = cInput
        self.simulations = vInput
        self.wins = wInput
        self.action = aInput
        self.turn = tInput  # 1 si es el turno del jugador y -1 si es el del enemigo
        self.uctValue = uInput
        self.isRoot = False
        self.flag = False

    # Gets y Sets

    def setState(self, SInput):
        self.state = SInput

    def getState(self):
        return self.state

    def setRoot(self, root):
        self.isRoot = root

    def getRoot(self):
        return self.isRoot

    def visit(self):
        self.flag = True

    def isVisited(self):
        return self.flag

    def unvisit(self):
        self.flag = False

    def setParent(self, PInput):
        self.parent = PInput

    def getParent(self):
        return self.parent

    def setChilds(self, CInput):
        self.childs = CInput

    def getChilds(self):
        return self.childs

    def setVisits(self, VInput):
        self.simulations = VInput

    def getVisits(self):
        return self.simulations

    def setWins(self, WInput):
        self.wins = WInput

    def getWins(self):
        return self.wins

    def setTurn(self, TInput):
        self.turn = TInput

    def setUct(self, UInput):
        self.utcValue = UInput

    def getUct(self):
        return self.utcValue

    #
    # Funciones Clase
    #

    def isFullExpanded(self):
        # Determina si el nodo esta completamente Expandido
        if ((len(self.childs) == (len(getActions(self.state))))):
            return True
        else:
            return False

    def ifActionIsInChilds(self, action):
        for c in self.childs:
            if (c.action == action):
                return True
        return False

    def expandNode(self):
        if self.turn == -1:
            actions = getActions(self.state)
            for a in actions:
                if self.ifActionIsInChilds(a) is False:
                    child = Node(transition(a, self.state), self, 0, [], 0, a, 1, 0)
                    self.childs.append(child)
                    return child
        else:
            actions = getActions_Enemigo(self.state)
            for a in actions:
                if self.ifActionIsInChilds(a) is False:
                    child = Node(transitionEnemigo(a, self.state), self, 0, [], 0, a, -1, 0)
                    self.childs.append(child)
                    return child

    def updateWins(self, outcome):
        self.simulations += 1
        self.wins += outcome


def UCTvalue(Tvisits, nodeWins, nodeVisits, nodeTurn):
    if nodeVisits == 0:
        return sys.maxsize
    else:
        return (nodeTurn * (nodeWins / nodeVisits)) + (phi * (math.sqrt(math.log(Tvisits) / nodeVisits)))


def findBestNode(rootNode):
    childs = rootNode.getChilds()
    sim = 0
    best = childs[0]
    for child in childs:
        if child.getVisits() > sim:
            best = child
    return best


def defaultPolicy(state, flag):
    while isTerminal(state) is False:
        if flag == 1:
            a = random.choice(getActions(state))
            state = transition(a, state)
            flag = 0
        else:
            a = random.choice(getActions_Enemigo(state))
            state = transitionEnemigo(a, state)
            flag = 1

    return state.whoWon()


def monteCarloTreeSearch(intialState, turn):
    t_end = time.time() + 4.8
    rootNode = Node(intialState, None, 0, [], 0, None, turn, 0)
    while time.time() < t_end:
        node, simulations = selectNode(rootNode)
        child = expandNode(node)
        outcome = defaultPolicy(child.getState(), child.turn)
        updateNodes(outcome, child, simulations)

    return findBestNode(rootNode)


def getTree(rootNode):
    nodes = [rootNode]
    rootNode.setRoot(True)
    currentNode = rootNode
    while rootNode.isVisited() is False:
        if not currentNode.getChilds():
            currentNode.visit()
            if currentNode is not rootNode:
                nodes.append(currentNode)
                currentNode = currentNode.getParent()
        else:
            complete = True
            for child in currentNode.getChilds():
                if not child.isVisited():
                    currentNode = child
                    complete = False
                    break
            if complete:
                currentNode.visit()
                if currentNode is not rootNode:
                    nodes.append(currentNode)
                    currentNode = currentNode.getParent()

    for node in nodes:
        node.unvisit()
    rootNode.setRoot(False)

    return nodes


def selectNode(rootNode):
    nodos = getTree(rootNode)
    visits = 0
    higher = 0
    bestnode = rootNode
    first = True
    for nodo in nodos:
        if first:
            first = False
            continue
        if nodo.getUct() > higher:
            higher = nodo.getUct()
            bestnode = nodo
        visits += nodo.getVisits()

    return bestnode, visits


def expandNode(node):
    if node.isFullExpanded():
        return expandNodeFull(node)
    else:
        return node.expandNode()


def expandNodeFull(node):
    new = selectNode(node)
    return expandNode(new)


def updateNodes(outcome, child, simulations):
    while child.getParent() is not None:
        child.updateWins(outcome)
        child.setUct = UCTvalue(simulations, child.getWins(), child.getVisits(), child.turn)
        child = child.parent


def main():
    with open('tablero.json') as f:
        datos = json.load(f)
        print(datos)
        for dato in datos:
            # print(dato['ids'])
            tablero = Estado([*zip(*dato['ids'])], [*zip(*dato['enemy_knights'])], [*zip(*dato['my_knights'])],
                             dato['enemy_knights_dict'],
                             dato['my_knights_dict'])

    tablero.printTablero()
    print(tablero.tablero[0][1])
    print(tablero.knight_enemigo_pos[str(102)])

    jugada = monteCarloTreeSearch(tablero, 1)
    jugada.getState().printTablero()

    tablero.printTablero()


if __name__ == "__main__":
    main()
