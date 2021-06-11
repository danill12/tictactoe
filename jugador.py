from mensajesES import msg


class Jugador:

    OPCIONES = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, marca, token):
        self.marca = marca
        self.token = token

    def elige(self, jugadasLibres):
        excep = None
        while excep is None:
            try:
                jugada = (input(msg["entrada"]))  # self.token
                excep = int(jugada)
            except ValueError:
                print(msg["errorFormato"])
        # print(f"  { self.token } { jugadasLibres }")

        return excep

    def imprimeTurno(self):
        print(msg["turno"])  # self.token
