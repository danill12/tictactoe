from os import system
from mensajesES import msg


class Tablero:

    OPCIONES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        self.reset()

    def reset(self):
        self.jugadas = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.muestra = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def dibuja(self):
        system("cls")
        print(msg["tablero"])
        print(f"""
        {self.muestra[0][0]} | {self.muestra[0][1]} | {self.muestra[0][2]}
        ----------
        {self.muestra[1][0]} | {self.muestra[1][1]} | {self.muestra[1][2]}
        ----------
        {self.muestra[2][0]} | {self.muestra[2][1]} | {self.muestra[2][2]}
        \n""")

    def jugadasLibres(self):
        return [j for i in self.jugadas for j in i]

    def introducirJugada(self, jugador, jugada):
        fila = self.ubicarFila(jugada)
        columna = self.ubicarColumna(jugada)
        self.jugadas[fila][columna] = jugador.marca
        self.muestra[fila][columna] = jugador.token

    def ubicarFila(self, jugada):
        if jugada <= 3:
            fila = 0
        elif jugada >= 4 and jugada <= 6:
            fila = 1
        else:
            fila = 2

        return fila

    def ubicarColumna(self, jugada):
        if jugada == 1 or jugada == 4 or jugada == 7:
            columna = 0
        elif jugada == 2 or jugada == 5 or jugada == 8:
            columna = 1
        else:
            columna = 2

        return columna

    def comprobarCasillaOcupada(self, jugada):
        if jugada not in self.OPCIONES:
            return True
        else:
            fila = self.ubicarFila(jugada)
            columna = self.ubicarColumna(jugada)
            if self.jugadas[fila][columna] == 0:
                return False
            else:
                return True
