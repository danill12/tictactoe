class Tablero:

    def __init__(self):
        self.reset()

    def reset(self):
        self.jugadas = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def dibuja(self):
        print(f"-- {{{ self.jugadas }}} ")

    def jugadasLibres(self):
        # https://blog.teamtreehouse.com/python-single-line-loops
        # https://stackoverflow.com/questions/716477/join-list-of-lists-in-python
        return [j for i in self.tablero.jugadas for j in i]
