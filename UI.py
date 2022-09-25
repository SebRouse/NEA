from Game import Game




class UI:
    def run(self):
        raise NotImplementedError("UI not implemented")

class Terminal(UI):
    def __init__(self):
        pass

    def turn(self,game):
        print(game.showBoard())

    def run(self):
        game = Game()
        game.addPlayers(2)
        game.updateLanguage(0)
        self.turn(game)
