class Jugador:

    OPCIONES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, marca, token):
        self.marca = marca
        self.token = token

    def elige(self, jugadasLibres):
        excep = None
        while excep is None:
            try:
                jugada = (input(f" jugador { self.token } elige pos: "))
                if jugada == 0:
                    print("Cagaste")
                else:
                    excep = int(jugada)
            except ValueError:
                print("Formato invalido")
        # print(f"  { self.token } { jugadasLibres }")

        return excep

    def imprimeTurno(self):
        print(f"Turno del jugador { self.token }")
