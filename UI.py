from Game import Game
from abc import ABC, abstractmethod




class UI(ABC):
    def run(self):
        raise NotImplementedError("UI not implemented")

class Terminal(UI):
    def __init__(self):
        pass

    def turn(self,game : Game):
        print(game.showBoard())
        print(f"Player 1: {game.players.displayPoints()}")
        print(f"Player {game.getTurnNo()}'s turn")

    def run(self):
        game = Game()
        game.addPlayers(2)
        game.updateLanguage(0)
        self.turn(game)
