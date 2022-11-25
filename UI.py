
from cProfile import label

from matplotlib.pyplot import text
from Game import Game
from abc import ABC, abstractmethod
from tkinter import *



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
        self.turn(game)

class GUI(UI):
    def __init__(self):
        pass


    def main():
        root = Tk()
        root.title("Scrabble - Main Menu")
        frame = Frame(root)
        frame.pack()

        Button(frame,text='Play Game',width = 40,height =3).pack(fill=X)

        Button(frame,text='Account',width = 40,height =3).pack(fill=X)

        Button(frame,text='Settings',width = 40,height =3).pack(fill=X)
        Button(frame,text='Login',width = 40,height =3).pack(fill=X)

        Button(frame,text='Quit',command=root.quit,width = 40,height =3).pack(fill=X)
        root.mainloop()
       

    def login():
        root= Tk()
        root.title("Scrabble- Login")

        label1 = Label(text ="Enter Username")
        label1.pack()
        canvas1 = Canvas(root, width=300, height=140)
        canvas1.pack()
        entry1 = Entry(root, width = 35) 
        canvas1.create_window(150,10, window=entry1)
        label2 = Label(text="Enter Password")
        label1.pack()
        canvas1.create_window(150,30,window = label2)
        entry2 = Entry(root, width= 35)
        entry2.pack()
        canvas1.create_window(150,50,window=entry2)
        button1=Button(root,text="login",width=10)
        button1.pack()
        canvas1.create_window(150,80,window = button1)
        button2=Button(root,text="quit",width=10,command=root.quit)
        button2.pack()
        canvas1.create_window(150,115,window = button2)

        root.mainloop()	


