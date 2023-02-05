
from Game import Game
from abc import ABC, abstractmethod
import pygame
from tkinter import *

class UI(ABC):
    def run(self):
        raise NotImplementedError("UI not implemented")

class Terminal(UI):
    def __init__(self):
        pass

    def turn(self,game:Game):
        print(game.printBoard())
        print(f"Player 1: {game.players[0].getPoints()} points: ")
        print(f"Player 2: {game.players[1].getPoints()} points: ")
        print(f"Player {game.getPTurn()+1}'s turn")
        print(f"Player {game.getPTurn()+1}'s rack: {game.players[game.getPTurn()].displayRack()}")

        print(f"Bag : {game.lenBag()} tiles")
        
        while True:
            currMoves = []
            while True:
                while True:
                    l = str(input(f"Player{game.getPTurn()+1} enter letter of next move and then Y and X coordinates on the following lines or -1 to end turn: "))
                    if len(l)==1 or l == "-1":
                        break
                if l == "blank":
                    l=str(input("Enter the letter the blank tile represents"))
                    l = l.lower()
                else:
                    l = l.upper()
                if str(l) == "-1":
                    break
                Y = int(input("Enter Y coordinate of turn: "))
                X = int(input("Enter X coordinate of turn: "))
                currMoves.append([l,Y,X])

            if len(currMoves) == 0:
                game.increaseNumPasses()
                break
            if not game.validateTurn(currMoves):
                print("Invalid Move")
            else:
                game.calculatePoints(currMoves)
                break


        game.incrementTurn()


        if game.isGameOver():
            
            winner = game.findWinner()
            print(f"Player 1: {game.players[0].getPoints()} points: ")
            print(f"Player 2: {game.players[1].getPoints()} points: ")
            print("*"*30)
            print(f"Player {winner+1} won")
            print("*"*30)
            exit()


        
        self.turn(game)


    def run(self):
        game = Game(None)
        numPlayers = 2
        game.updateLanguage("English")
        game.addPlayers(numPlayers)
        
    

        self.turn(game)





game=Terminal()
game.run()








