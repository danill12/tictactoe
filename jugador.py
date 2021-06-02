class Jugador:
    def __init__(self, marca):
        self.marca = marca

    def elige(self, jugadasLibres):

        jugada = input(f" jugador {self.marca} elige pos: ")

        print(f"  { self.marca } { jugadasLibres }")
