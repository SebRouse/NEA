from Game import Game
from tkinter import *
from databse import Account
import time
import pygame





class GUI():
    def __init__(self):
        self._root=Tk()
        self._loginWindow = None
        self._LEntryU=None  #login window - username entry box
        self._LEntryP=None # login window - password entry box
        self._creatAccountWindow=None
        self._CEntryU=None  # create account window - username entry box
        self._CEntryP=None  # create account window - password entry box
        self._account = Account()


        self.main()
        



    def loginErrorUsername(self):
        lError= Toplevel(self._root)
        lError.title("Scrabble-Login Error")
        lError.geometry("200x80")
        Label(lError,text="Error:\n Your username/password is\n incorrect or does not exist").pack()
        Button(lError,text ="Dismiss",command=lError.destroy).pack()

    def AccountError(self):
        aError = Toplevel(self._root)
        aError.title("Scrabble - Account Creation Error")
        aError.geometry("200x80")
        Label(aError,text="Error:\n An account with that\n username already exists").pack()
        Button(aError,text="Dismiss",command=aError.destroy).pack()

    def checkLogin(self):
        username = self._LEntryU.get()
        password = self._LEntryP.get()
        
        check =False
        if check:
            self.quitLogin()
            self.loginSuccesful()

        else:
            self.loginErrorUsername()
            
            

    


    def loginSuccesful(self):
        loginSuccesful= Toplevel(self._root)
        loginSuccesful.title("Scrabble - Login Succesful")
        loginSuccesful.geometry("200x80")
        Label(loginSuccesful,text="Login \n Succesful \n").pack()
        Button(loginSuccesful,text="Dismiss",command=loginSuccesful.destroy).pack()

    def quitLogin(self):
        self._loginWindow.destroy()
        self._loginWindow=None




    def login(self):
        if self._loginWindow != None:
            return False


        self._loginWindow=Toplevel(self._root)
        
        self._loginWindow.title("Scrabble- Login")
        self._loginWindow.geometry("300x150")
        canvas1 = Canvas(self._loginWindow, width=300, height=150)
        
        label1 = Label(self._loginWindow,text ="Enter Username")
        label1.pack()
        canvas1.create_window(150,10,window=label1)

        self._LEntryU = Entry(self._loginWindow, width = 35) 
        self._LEntryU.pack
        canvas1.create_window(150,30, window=self._LEntryU)
        label2 = Label(self._loginWindow,text="Enter Password")
        label2.pack()
        canvas1.create_window(150,50,window = label2)
        self._LEntryP = Entry(self._loginWindow, width= 35)
        self._LEntryP.pack()
        canvas1.create_window(150,70,window=self._LEntryP)
        button1=Button(self._loginWindow,text="Login",width=10,command=self.checkLogin)
        button1.pack()
        canvas1.create_window(150,100,window = button1)
        button2=Button(self._loginWindow,text="Quit",width=10,command=self.quitLogin)
        button2.pack()
        canvas1.create_window(150,135,window = button2)
        canvas1.pack()


    def CreateAccount(self):
        self._createAccountWindow=Toplevel(self._root)
        self._createAccountWindow.title("Scrabble- Create Account")
        self._createAccountWindow.geometry("300x150")
        canvas1 = Canvas(self._createAccountWindow, width=300, height=150)
        
        label1 = Label(self._createAccountWindow,text ="Enter Username")
        label1.pack()
        canvas1.create_window(150,10,window=label1)

        entry1 = Entry(self._createAccountWindow, width = 35) 
        entry1.pack
        canvas1.create_window(150,30, window=entry1)
        label2 = Label(self._createAccountWindow,text="Enter Password")
        label2.pack()
        canvas1.create_window(150,50,window = label2)
        entry2 = Entry(self._createAccountWindow, width= 35)
        entry2.pack()
        canvas1.create_window(150,70,window=entry2)
        button1=Button(self._createAccountWindow,text="Create \n Account",width=10,command=self.AccountError)
        button1.pack()
        canvas1.create_window(150,100,window = button1)
        button2=Button(self._createAccountWindow,text="Quit",width=10,command=self._createAccountWindow.destroy)
        button2.pack()
        canvas1.create_window(150,135,window = button2)
        canvas1.pack()



    def SelectLanguage(self):
        languageWindow=Toplevel(self._root)
        languageWindow.title("Scrabble - Play Game - Select Language")
        languageWindow.geometry("200x250")
        Label(languageWindow,text = "Select language:").pack(pady=1)

        Button(languageWindow,text="English",width=20,height=2).pack(pady=20)
        Button(languageWindow,text="Spanish",width=20,height=2).pack()
    

    def PlayGame(self):
        pass

    def UndoError(self):
        UError=Toplevel(self._root)
        UError.title("Scrabble - Play Game - Undo Error")
        UError.geometry("200x60")
        Label(UError,text="Error:\n There are no moves left to undo").pack
        Button(UError,text ="Dismiss",command=UError.destroy).pack()

    def main(self):


        self._root.title("Scrabble - Main Menu")
        frame = Frame(self._root)
        frame.pack()



        Button(frame,text='Play Game',width = 40,height =3,command=self.SelectLanguage).pack(fill=X)
        Button(frame,text='Account',width = 40,height =3).pack(fill=X)
        Button(frame,text='Create Acount',width = 40,height =3,command=self.CreateAccount).pack(fill=X)
        Button(frame,text='Login',width = 40,height =3, command=self.login).pack(fill=X)
        Button(frame,text='Help',width = 40,height =3).pack(fill=X)
        Button(frame,text='Quit',command=self._root.quit,width = 40,height =3).pack(fill=X)
        self._root.mainloop()


gui = GUI()