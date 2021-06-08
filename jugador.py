class Jugador:

    def __init__(self, marca):
        self.marca = marca

    def elige(self, jugadasLibres):

        jugada = int(input(f" jugador {self.marca} elige pos: "))

        print(f"  { self.marca } { jugadasLibres }")

        return jugada

    def imprimeAlgo(self):
        print(f"Turno del jugador { self.marca }")
