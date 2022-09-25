from Game import Game




class UI:
    def run(self):
        raise NotImplementedError("UI not implemented")

class Terminal(UI):
    def __init__(self):
        pass

    def turn(self,game):
        pass

    def run(self):
        game = Game()
        self.turn(game)
