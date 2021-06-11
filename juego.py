from tablero import Tablero
from jugador import Jugador
from mensajesES import msg
from os import system


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
        system("cls")
        print(msg["inicio"])
        system("Pause")
        self.tablero.dibuja()
        while self.turno < self.DURACION:
            self.EjecutarTurno()
        print(msg["empate"])

    def EjecutarTurno(self):
        jugador = self.jugadores[self.turno % 2]
        jugador.imprimeTurno()
        self.turno += 1

        jugadasLibres = self.tablero.jugadasLibres()
        jugada = jugador.elige(jugadasLibres)

        while self.tablero.comprobarCasillaOcupada(jugada):
            print(msg["errorCasilla"])
            jugada = jugador.elige(jugadasLibres)

        self.tablero.introducirJugada(jugador, jugada)
        self.tablero.dibuja()

        self.comprobarResutado(jugador)

    def comprobarResutado(self, jugador):
        lineasGanadoras = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
        ]

        for lineasGanadora in lineasGanadoras:
            suma = 0
            for tupla in lineasGanadora:
                casilla = self.tablero.jugadas[tupla[0]][tupla[1]]
                suma += casilla
                if suma in self.SUMA:
                    print(msg["victoria"])  # jugador.token
                    exit()
