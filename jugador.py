class Jugador:

    OPCIONES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, marca, token):
        self.marca = marca
        self.token = token

    def elige(self, jugadasLibres):

        jugada = int(input(f" jugador { self.token } elige pos: "))

        # print(f"  { self.token } { jugadasLibres }")

        return jugada

    def imprimeTurno(self):
        print(f"Turno del jugador { self.token }")
