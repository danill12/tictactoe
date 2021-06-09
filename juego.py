from tablero import Tablero
from jugador import Jugador


class Juego:

    DURACION = 9
    TOKEN = ["X", "O"]
    VALOR = [1, -1]
    SUMA = [3, -3]

    def __init__(self):
        self.tablero = Tablero()
        self.reset()
        self.juega()

    def reset(self):
        self.jugadores = [
            Jugador(self.VALOR[0], self.TOKEN[0]),
            Jugador(self.VALOR[1], self.TOKEN[1])
        ]
        self.tablero.reset()
        self.turno = 0

    def juega(self):
        self.tablero.dibuja()
        while self.turno < self.DURACION:
            self.EjecutarTurno()

    def EjecutarTurno(self):
        jugador = self.jugadores[self.turno % 2]
        jugador.imprimeTurno()
        self.turno += 1

        jugadasLibres = self.tablero.jugadasLibres()
        jugada = jugador.elige(jugadasLibres)

        while self.tablero.comprobarCasillaOcupada(jugada):
            print("ERROR, Intenta de nuevo")
            jugada = jugador.elige(jugadasLibres)

        self.tablero.introducirJugada(jugador, jugada)
        print("El tablero actual: \n")
        for fila in self.tablero.jugadas:
            print(fila)

        self.comprobarResutado(jugador)

    def comprobarResutado(self, jugador):
        if sum(self.tablero.jugadas[0]) in self.SUMA:
            print("Ha ganado ", jugador.token)
            exit()
        elif sum(self.tablero.jugadas[1]) in self.SUMA:
            print("Ha ganado ", jugador.token)
            exit()
        elif sum(self.tablero.jugadas[2]) in self.SUMA:
            print("Ha ganado ", jugador.token)
            exit()
        elif self.tablero.jugadas[0][0] + self.tablero.jugadas[1][1] + self.tablero.jugadas[2][2] in self.SUMA:
            print("Ha ganado ", jugador.token)
            exit()
        elif self.tablero.jugadas[0][2] + self.tablero.jugadas[1][1] + self.tablero.jugadas[2][0] in self.SUMA:
            print("Ha ganado ", jugador.token)
            exit()
        elif self.tablero.jugadas[0][0] + self.tablero.jugadas[1][0] + self.tablero.jugadas[2][0] in self.SUMA:
            print("Ha ganado ", jugador.token)
            exit()
        elif self.tablero.jugadas[0][1] + self.tablero.jugadas[1][1] + self.tablero.jugadas[2][1] in self.SUMA:
            print("Ha ganado ", jugador.token)
            exit()
        elif self.tablero.jugadas[0][2] + self.tablero.jugadas[1][2] + self.tablero.jugadas[2][2] in self.SUMA:
            print("Ha ganado ", jugador.token)
            exit()
