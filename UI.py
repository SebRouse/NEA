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
        print(f"Player 1: {game.players[game.getPTurn()].displayPoints()}")
        print(f"Player {game.getPTurn()+1}'s turn")
        

    def run(self):
        game = Game()
        numPlayers = 2
        game.addPlayers(numPlayers)
        game.updateLanguage(0)
        for i in range (numPlayers):
            game.updatePlayerRack(i)
        self.turn(game)
