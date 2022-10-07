from multiprocessing.pool import TERMINATE
from Game import Game
from abc import ABC, abstractmethod




class UI(ABC):
    def run(self):
        raise NotImplementedError("UI not implemented")

class Terminal(UI):
    def __init__(self):
        pass

    def turn(self,game : Game):
        print(game.printBoard())
        print(f"Player 1: {game.players[0].getPoints()} points")
        print(f"Player 2: {game.players[1].getPoints()} points")
        print(f"Player {game.getPTurn()+1}'s turn")
        while True:
            l = str(input("Enter letter of next move and then Y and X coordinates on the following lines or -1 to end turn: ")).upper()
            if str(l) == "-1":
                break
            Y = int(input("Enter Y coordinate of turn"))
            X = int(input("Enter X coordinate of turn"))
            game.currMoves.append([l,Y,X])
        if not game.validateTurn():
            print("Invalid Move")
        else:
            game.calculatePoints()
        
        if game.isGameOver:
            winner = game.findWinner()
            print("*"*30)
            print(f"Player {winner} won")
            print("*"*30)
            TERMINATE
        game.endTurn()


    def run(self):
        game = Game()
        numPlayers = 2
        game.addPlayers(numPlayers)
        game.updateLanguage(0)
        for i in range (numPlayers):
            game.updatePlayerRack(i)
        self.turn(game)


g=Terminal()
g.run()