from tablero import Tablero
from jugador import Jugador


class Juego:

    DURACION = 9
    MARCA = ['X', 'O']

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
            self.turno += 1

            # https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
            # jugadasLibres = [j for i in self.tablero.jugadas for j in i]

            jugadasLibres = []
            for fila in self.tablero.jugadas:
                jugadasLibres += fila

            jugada = jugador.elige(jugadasLibres)

            # self.tablero.dibuja()
