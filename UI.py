


#from matplotlib.pyplot import text
#from Game import Game
from abc import ABC, abstractmethod
from turtle import color
#from tkinter import *
import pygame

class UI(ABC):
    def run(self):
        raise NotImplementedError("UI not implemented")

'''class Terminal(UI):
    def __init__(self):
        pass

    def turn(self,game : Game):
        print(game.printBoard())
        print(f"Player 1: {game.players[0].getPoints()} points")
        print(f"Player 2: {game.players[1].getPoints()} points")
        print(f"Player {game.getPTurn()+1}'s turn")
        print(f"Player {game.getPTurn()+1}'s rack: {game.players[game.getPTurn()].displayRack()}")
        currMoves = []
        while True:
            l = str(input("Enter letter of next move and then Y and X coordinates on the following lines or -1 to end turn: "))
            if l == "blank":
                l=str(input("Enter the letter the blank tile represents"))
                l = l.lower()
            else:
                l = l.upper()
            if str(l) == "-1":
                break
            Y = int(input("Enter Y coordinate of turn"))
            X = int(input("Enter X coordinate of turn"))
            currMoves.append([l,Y,X])
        if not game.validateTurn(currMoves):
            print("Invalid Move")
        else:
            game.calculatePoints(currMoves)
        
        if game.isGameOver():
            winner = game.findWinner()
            print("*"*30)
            print(f"Player {winner+1} won")
            print("*"*30)
            exit()

        game.incrementTurn()
        
        self.turn(game)


    def run(self):
        game = Game()
        numPlayers = 2
        game.addPlayers(numPlayers)
        game.updateLanguage(0)
        for i in range (numPlayers):
            game.updatePlayerRack(i)
        self.turn(game)'''







pygame.init()
screen = pygame.display.set_mode((1200,1000))
# game loop
pygame.display.set_caption("Scrabble")
running = True
board_tiles = [[0 for row in range(15)] for col in range(15)]
block_size = 60
board_tiles[4][5]=1
for row in range(len(board_tiles)):
    for col in range(len(board_tiles[0])):
        tile = board_tiles[row][col]
        if tile == 0:
            color = (255, 255, 255)
        elif tile == 1:
            color = (0, 255, 0)
        rect = pygame.Rect(col*(block_size+1), row*(block_size+1), block_size, block_size)

        pygame.draw.rect(screen, color, rect)
font = pygame.font.SysFont(None, 24)
img = font.render('Points:', True, (0,0,255))
screen.blit(img, (915, 20))
pygame.display.update()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
