import json
import math
import random
import time
import sys

# Variables Globales
    
# 

class Accion:
    def __init__(self):
        self.knight_id = 0
        self.knight_movement = 0

    def setKnight_id(self,id):
        self.knight_id = id
    def setKnight_movement(self,mov):
        self.knight_movement = mov
    def getKnight_id(self):
        return self.knight_id
    def getKnight_movement(self):
        return self.knight_movement
    
    def printAccion(self):
        print('Pieza: ',self.knight_id , 'puede realizar el movimiento: ',self.knight_movement)

class Estado:
    def __init__(self,tablero_nuevo,enemigo,aliado,pos_enemigo,pos_aliado):
        self.tablero = tablero_nuevo
        self.knight_enemigo = enemigo
        self.knight_enemigo_pos = pos_enemigo
        self.knight_aliado = aliado
        self.knight_aliado_pos = pos_aliado

    def printTablero(self):
        print(self.tablero)   

    def printAliado(self):
        print(self.knight_aliado)

    def printKnight_aliado_pos(self):
        print(self.knight_aliado_pos)     

    def printEnemigo(self):
        print(self.knight_enemigo)

    def printKknight_enemigo_pos(self):
        print(self.knight_enemigo_pos)

    def getTablero(self):
        return self.tablero

    def getPos_knight_enemigo(self,id):
        return self.knight_enemigo_pos[id]

    def getPos_knight_aliado(self,id):  
        return self.knight_aliado_pos[id]

    def getEnemigo(self):
        return self.knight_enemigo

    def getAliado(self):
        return self.knight_aliado

    def esAliado(self,x,y):
        if self.knight_aliado[y][x] != None:
            return True
        return False

    def insertarKinght_tablero(self,x,y,id):
        if self.tablero[y][x] != None:
            del self.knight_enemigo_pos[str(self.tablero[y][x])]
            self.knight_enemigo[y][x] = None
            self.tablero[y].pop(x)
        self.tablero[y].insert(x,id)
        self.knight_aliado_pos[str(id)] = [x,y]
        self.knight_aliado[y].insert(x,id)

    def eliminarKnight_tablero(self,x,y):
        self.tablero[y][x] = None

    def esEnemigo(self,x,y):
        if self.knight_enemigo[y][x] !=None:
            return True
        return False

    def insertarKinght_tablero_Enemigo(self,x,y,id):
        if self.tablero[y][x] != None:
            del self.knight_aliado_pos[str(self.tablero[y][x])]
            self.knight_aliado[y][x] = None
            self.tablero[y].pop(x)
        self.tablero[y].insert(x,id)
        self.knight_enemigo_pos[str(id)] = [x,y]
        self.knight_enemigo[y].insert(x,id)

    def eliminarKnight_tablero(self,x,y):
        self.tablero[y][x] = None
    
def getActions(estado):
    lista_acciones = []
    for i in range(200, 216):
        knight_pos = estado.getPos_knight_aliado(str(i))
        #print(knight_pos)
        x = knight_pos[0]
        #print (x)
        y = knight_pos[1]
        #print(y)
        directions = [0, 1, 2, 3, 4, 5, 6, 7]
        tablero = estado.getTablero()
        
        if x+1 < 8 and y+2 < 8:
            if estado.esAliado(x+1,y+2):
                directions.remove(0)
        else:
            if x+1 >= 8 or y+2 >=8:
                directions.remove(0)
        
        if x+2 < 8 and y+1 < 8:
            if estado.esAliado(x+2,y+1):
                directions.remove(1)
        else:
            if x+1 >= 8 or y+2 >=8:
                directions.remove(1)
            
        if x+2 < 8 and y-1 >= 0: 
            if estado.esAliado(x+2,y-1):
                directions.remove(2)
        else:
            if x+2 >= 8 or y-1 < 0:
                directions.remove(2)
        
        if x+1 < 8 and y-2 >= 0:  
            if estado.esAliado(x+1,y-2):
                directions.remove(3)
        else:
            if x+1 >= 8 or y-2 < 0:
                directions.remove(3)

        if x-1 >=0 and y-2 >= 0:
            if estado.esAliado(x-1,y-2):
                directions.remove(4)
        else:
            if x-1 < 0 or y-2 < 0:
                directions.remove(4)

        if x-2 >=0 and y-1 >= 0:
            if estado.esAliado(x-2,y-1):
                directions.remove(5)
        else:
            if x-2 < 0 or y-1 < 0:
                directions.remove(5) 

        if x-2 >=0 and y+1 < 8:
            if estado.esAliado(x-2,y+1):
                directions.remove(6)
        else:
            if x-2 < 0 or y+1 >= 8:
                directions.remove(6)

        if x-1 >=0 and y+2 < 8: 
            if estado.esAliado(x-1,y+2):
                directions.remove(7)
        else:
            if x-1 < 0 or y+2 >= 8:
                directions.remove(7)

        for direction in directions:
            accion = Accion()
            accion.setKnight_id(str(i))
            accion.setKnight_movement(direction)
            lista_acciones.append(accion)
        
    return lista_acciones



def transition(accion,estado):
    nuevo_estado = estado
    knight_pos = estado.getPos_knight_aliado(str(accion.getKnight_id()))
    #print(knight_pos)
    x = knight_pos[0]
    #print (x)
    y = knight_pos[1]

    if accion.getKnight_movement() == 0:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x+1
        y = y+2
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())

    if accion.getKnight_movement() == 1:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x+2
        y = y+1
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())

    if accion.getKnight_movement() == 2:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x+2
        y = y-1
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 3:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x+1
        y = y-2
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 4:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x-1
        y = y-2
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 5:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x-2
        y = y-1
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 6:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x-2
        y = y+1
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 7:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x-1
        y = y+2
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())

    return nuevo_estado

def isTerminal(estado):
    if estado.getPos_knight_aliado():
        return False
    if estado.getPos_knight_enemigo():
        return False
    return True


def getActions_Enemigo(estado):
    lista_acciones = []
    for i in range(100, 115):
        knight_pos = estado.getPos_knight_enemigo(str(i))
        #print(knight_pos)
        x = knight_pos[0]
        #print (x)
        y = knight_pos[1]
        #print(y)
        directions = [0, 1, 2, 3, 4, 5, 6, 7]
        tablero = estado.getTablero()
        
        if x+1 < 8 and y+2 < 8:
            if estado.esAliado(x+1,y+2):
                directions.remove(0)
        else:
            if x+1 >= 8 or y+2 >=8:
                directions.remove(0)
        
        if x+2 < 8 and y+1 < 8:
            if estado.esAliado(x+2,y+1):
                directions.remove(1)
        else:
            if x+1 >= 8 or y+2 >=8:
                directions.remove(1)
            
        if x+2 < 8 and y-1 >= 0: 
            if estado.esAliado(x+2,y-1):
                directions.remove(2)
        else:
            if x+2 >= 8 or y-1 < 0:
                directions.remove(2)
        
        if x+1 < 8 and y-2 >= 0:  
            if estado.esAliado(x+1,y-2):
                directions.remove(3)
        else:
            if x+1 >= 8 or y-2 < 0:
                directions.remove(3)

        if x-1 >=0 and y-2 >= 0:
            if estado.esAliado(x-1,y-2):
                directions.remove(4)
        else:
            if x-1 < 0 or y-2 < 0:
                directions.remove(4)

        if x-2 >=0 and y-1 >= 0:
            if estado.esAliado(x-2,y-1):
                directions.remove(5)
        else:
            if x-2 < 0 or y-1 < 0:
                directions.remove(5) 

        if x-2 >=0 and y+1 < 8:
            if estado.esAliado(x-2,y+1):
                directions.remove(6)
        else:
            if x-2 < 0 or y+1 >= 8:
                directions.remove(6)

        if x-1 >=0 and y+2 < 8: 
            if estado.esAliado(x-1,y+2):
                directions.remove(7)
        else:
            if x-1 < 0 or y+2 >= 8:
                directions.remove(7)

        for direction in directions:
            accion = Accion()
            accion.setKnight_id(str(i))
            accion.setKnight_movement(direction)
            lista_acciones.append(accion)
        
    return lista_acciones

def transitionEnemigo(accion,estado):
    nuevo_estado = estado
    knight_pos = estado.getPos_knight_enemigo(str(accion.getKnight_id()))
    #print(knight_pos)
    x = knight_pos[0]
    #print (x)
    y = knight_pos[1]

    if accion.getKnight_movement() == 0:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x+1
        y = y+2
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())

    if accion.getKnight_movement() == 1:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x+2
        y = y+1
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())

    if accion.getKnight_movement() == 2:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x+2
        y = y-1
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 3:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x+1
        y = y-2
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 4:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x-1
        y = y-2
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 5:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x-2
        y = y-1
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 6:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x-2
        y = y+1
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())


    if accion.getKnight_movement() == 7:
        nuevo_estado.eliminarKnight_tablero(x,y)
        x = x-1
        y = y+2
        nuevo_estado.insertarKinght_tablero(x,y,accion.getKnight_id())

    return nuevo_estado

# 
# Estructuras Para Implementar Arbol  
# 

class Node:
    def __init__(self, sInput, pInput, wInput, sInput, vInput, aInput):
        self.state = sInput
        self.parent = pInput
        self.childs = cInput
        self.visits = vInput
        self.wins = wInput
        self.action = aInput

    # Gets y Sets

    def setState(self, SInput):
        self.state = SInput

    def getState(self):
        return self.state
        
    def setParent(self, PInput):
        self.parent = PInput

    def getParent(self):
        return self.parent
        
    def setChilds(self, CInput):
        self.childs = CInput

    def getChilds(self):
        return self.childs
    
    def setVisits(self,VInput):
        self.visits = VInput

    def getVisits(self):
        return self.visits
        
    def setWins(self, WInput):
        self.wins = WInput

    def getWins(self):
        return self.wins

    #
    # Funciones Clase
    #

    def isFullExpanded(self):
        # Determina si el nodo esta completamente Expandido
        if((len(self.childs)==(len(getActions(self.state))))):
            return True
        else
            return False

    def expandNode(self):
        actions = getActions(self.state)
        for a in actions:
            child = node(transition(a, parentState), n, 0, [], 0, a)
            self.childs.append(child)

    def updateWins(self, reward):
        self.visits += 1
        self.wins += reward

def UCTvalue(Tvisits, nodeWins, nodeVisits):
    
    if nodeVisits == 0:
        return sys.maxsize
    else:
        return (nodeWins / nodeVisits) + 1.41*(math.sqrt(math.log(Tvisits)/nodeVisits))

def findBestNode(Snode):
    parentVisit = Snode.getVisits()
    childs = Snode.getChilds()
    bestScore =  0
    ret = []

    for child in childs:
        score = UCTvalue(parentVisit, child.getWins(), child.getVisitis())
        if(score == bestScore):
            ret.append(child)    
        if(score > bestScore):
            ret = [child]
            bestScore = score

    return random.choice(ret)

def backUP(node, reward):
    #
    # Recordar que nodo raiz tiene como padre None
    #

    while node!= None:
        node.updateWins(reward)
        node = node.parent

def treepolicy(node):
    while(isTerminal(node.getState())==False):
        if( len( node.getChilds()) == 0 ):
            node.expandNode()
            return node
        elif random.uniform(0,1) <.5:
            node = findBestNode(node)
        else:
            if node.isFullExpanded() == False:
                node.expandNode()
                return node
            else:
                node = findBestNode(node)
    return node

#
# simula aqui
#

def deafultPolicy(inputState):
    while isTerminal(inputState)==False:
        



def monteCarloTreeSearch(intialState):
    t_end = time.time() + 4.8
    rootNode = Node(intialState, None, 0, [], 0, None)
    while time.time() < t_end:
        vL = treepolicy(rootNode)
        reward = deafultPolicy(vL.state)


    return findBestNode(rootNode)



def main():
    with open('tablero.json') as f:
        datos = json.load(f)
        print(datos)
        for dato in datos:
            # print(dato['ids'])
            tablero = Estado(dato['ids'], dato['enemy_knights'], dato['my_knights'], dato['enemy_knights_dict'],
                             dato['my_knights_dict'])

    posicion_enemiga = tablero.getPos_knight_enemigo('100')
    print('posicion enemiga: ', posicion_enemiga)

    tablero.printTablero()
    print(tablero.tablero[0][1])
    print(tablero.tablero[4][4])

    test = 200
    print((tablero.knight_aliado_pos[str(test)]))

    acciones = getActions(tablero)
    for accion in acciones:
        accion.printAccion()

if __name__ == "__main__":
    main()
