from tablero import Tablero
from jugador import Jugador


class Juego:

    DURACION = 9
    MARCA = [1, -1]
    OPCIONES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.tablero = Tablero()
        self.reset()
        self.juega()

    def reset(self):
        self.jugador = [
            Jugador(self.MARCA[0]),
            Jugador(self.MARCA[1])
        ]
        self.tablero.reset()
        self.turno = 0

    def juega(self):
        self.tablero.dibuja()
        while self.turno < self.DURACION:
            jugador = self.jugador[self.turno % 2]

            jugador.imprimeAlgo()

            self.turno += 1

            # https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
            # jugadasLibres = [j for i in self.tablero.jugadas for j in i]

            jugadasLibres = []
            for fila in self.tablero.jugadas:
                jugadasLibres += fila

            jugada = jugador.elige(jugadasLibres)

            while jugada not in self.OPCIONES:
                print("Introduzaca una jugada valida")
                jugada = jugador.elige(jugadasLibres)

            # self.tablero.dibuja()
            print("El tablero: ", self.tablero.jugadas)
            print("La jugada:", jugada)
            print("El jugador: ", jugador.marca)

            if jugada <= 3:
                fila = 0
            elif jugada >= 4 and jugada <= 6:
                fila = 1
            else:
                fila = 2
            print(fila)

            if jugada == 1 or jugada == 4 or jugada == 7:
                columna = 0
            elif jugada == 2 or jugada == 5 or jugada == 8:
                columna = 1
            else:
                columna = 2
            print(columna)

            self.tablero.jugadas[fila][columna] = jugador.marca

            print("El tablero actual:", self.tablero.jugadas)

            self.comprobarResutado()

    def comprobarResutado(self):
        if self.tablero.jugadas[0][0] + self.tablero.jugadas[0][1] + self.tablero.jugadas[0][2] == 3:
            print("Ha ganado X")
            exit()
        elif self.tablero.jugadas[0][0] + self.tablero.jugadas[0][1] + self.tablero.jugadas[0][2] == -3:
            print("Ha ganado X")
            exit()
