import json


class Accion:
    def __init__(self):
        self.knight_id = 0
        self.knight_movement = 0

    def __init__(self, knight_id, knight_movement):
        self.knight_movement = knight_movement
        self.knight_id = knight_id

    def setKnight_id(self, knight_id):
        self.knight_id = knight_id

    def setKnight_movement(self, knight_movement):
        self.knight_movement = knight_movement

    def getKnight_id(self):
        return self.knight_id

    def getKnight_movement(self):
        return self.knight_movement

    def printAccion(self):
        print(self.knight_movement)
        print(self.knight_id)
        print()

class Estado:
    def __init__(self, tablero_nuevo, enemigo, aliado, pos_enemigo, pos_aliado):
        self.tablero = tablero_nuevo
        self.knight_enemigo = enemigo
        self.knight_enemigo_pos = pos_enemigo
        self.knight_aliado = aliado
        self.knight_aliado_pos = pos_aliado

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


def getActions(estado):
    lista_acciones = []
    for i in range(200, 216):
        knight_pos = estado.getPos_knight_aliado(i)
        x = knight_pos[0]
        y = knight_pos[1]
        directions = [0, 1, 2, 3, 4, 5, 6, 7]
        tablero = estado.getTablero()

        if x+2 < 8 and y+1 < 8 and tablero[x + 2][y + 1] is not None:
            directions.remove(0)
        if x+1 < 8 and y+2 < 8 and tablero[x + 1][y + 2] is not None:
            directions.remove(1)
        if x-1 >= 0 and y+2 < 8 and tablero[x - 1][y + 2] is not None:
            directions.remove(2)
        if x-2 >= 0 and y+1 < 8 and tablero[x - 2][y + 1] is not None:
            directions.remove(3)
        if x-2 >= 0 and y-1 >= 0 and tablero[x - 2][y - 1] is not None:
            directions.remove(4)
        if x-1 >= 0 and y-2 >= 0 and tablero[x - 1][y - 2] is not None:
            directions.remove(5)
        if x+1 < 8 and y-2 >= 0 and tablero[x + 1][y - 2] is not None:
            directions.remove(6)
        if x+2 < 8 and y-1 >= 0 and tablero[x + 2][y - 1] is not None:
            directions.remove(7)

        for direction in directions:
            accion = Accion(str(i), direction)
            lista_acciones.append(accion)

    return lista_acciones

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
