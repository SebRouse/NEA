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
        self._createAccountWindow=None
        self._CEntryU=None  # create account window - username entry box
        self._CEntryP=None  # create account window - password entry box
        self._account = Account()
        self._screen=None
        self._languageWindow = None


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
        if username.strip() == "" or password.strip()=="":
            return False
        check =self._account.Login(username,password)
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


    def CreateAccountWindow(self):
        if self._createAccountWindow:
            return False

        self._createAccountWindow=Toplevel(self._root)
        self._createAccountWindow.title("Scrabble- Create Account")
        self._createAccountWindow.geometry("300x150")
        canvas1 = Canvas(self._createAccountWindow, width=300, height=150)
        
        label1 = Label(self._createAccountWindow,text ="Enter Username")
        label1.pack()
        canvas1.create_window(150,10,window=label1)

        self._CEntryU = Entry(self._createAccountWindow, width = 35) 
        self._CEntryU.pack
        canvas1.create_window(150,30, window=self._CEntryU)
        label2 = Label(self._createAccountWindow,text="Enter Password")
        label2.pack()
        canvas1.create_window(150,50,window = label2)
        self._CEntryP = Entry(self._createAccountWindow, width= 35)
        self._CEntryP.pack()
        canvas1.create_window(150,70,window=self._CEntryP)
        button1=Button(self._createAccountWindow,text="Create \n Account",width=10,command=self.checkCreateAccount)
        button1.pack()
        canvas1.create_window(150,100,window = button1)
        button2=Button(self._createAccountWindow,text="Quit",width=10,command=self.quitCreateAccount)
        button2.pack()
        canvas1.create_window(150,135,window = button2)
        canvas1.pack()

    def quitCreateAccount(self):
        self._createAccountWindow.destroy()
        self._createAccountWindow=None


    def checkCreateAccount(self):
        
        username = self._CEntryU.get()
        password = self._CEntryP.get()
        if username.strip() == "" or password.strip()=="":
            return False
        check = self._account.CreateAccount(username,password)
        if check:
            self.CreateAccountSuccesful()
            self.quitCreateAccount()
        else:
            self.AccountError()



    def CreateAccountSuccesful(self):
        createAccountSuccesful= Toplevel(self._root)
        createAccountSuccesful.title("Scrabble - Create Account Succesful")
        createAccountSuccesful.geometry("200x80")
        Label(createAccountSuccesful,text="Account Created \n Succesfuly \n").pack()
        Button(createAccountSuccesful,text="Dismiss",command=createAccountSuccesful.destroy).pack()





    def SelectLanguage(self):
        self._languageWindow=Toplevel(self._root)
        self._languageWindow.title("Scrabble - Play Game - Select Language")
        self._languageWindow.geometry("200x250")
        Label(self._languageWindow,text = "Select language:").pack(pady=1)

        Button(self._languageWindow,text="English",width=20,height=2,command=self.PlayGameEnglish).pack(pady=20)
        Button(self._languageWindow,text="Spanish",width=20,height=2,command =self.PlayGameSpanish).pack()
    
    def PlayGameEnglish(self):
        self._languageWindow.destroy()
        game=Game(self._account)
        game.updateLanguage("English")
        game.addPlayers(2)

        self.PlayGame()
    
    def PlayGameSpanish(self):
        self._languageWindow.destroy()
        game=Game(self._account)
        game.updateLanguage("Spanish")
        game.addPlayers(2)

        self.PlayGame()

    def UndoError(self):
        UError=Toplevel(self._root)
        UError.title("Scrabble - Play Game - Undo Error")
        UError.geometry("200x60")
        Label(UError,text="Error:\n There are no moves left to undo").pack()
        Button(UError,text ="Dismiss",command=UError.destroy).pack()


    def AccountCheck(self):
        if self._account.getAccount():
            self.AccountWindow()
        else:
            self.NotLoggedIn()

    def NotLoggedIn(self):
        AError=Toplevel(self._root)
        AError.title("Scrabble - Account - Login Error")
        AError.geometry("200x80")
        Label(AError,text="Error:\n you are not logged in\n").pack()
        Button(AError,text ="Dismiss",command=AError.destroy).pack()          

    def AccountWindow(self):
        accountWindow = Toplevel(self._root)
        accountWindow.title("Scrabble - Account")
        accountWindow.geometry("300x300")
        result = self._account.GetWinLoss()
        games,wins,losses = result[0]
        name =self._account.getAccount()
        Label(accountWindow,font=('Helvetica',44),text=f"{name}:").pack()
        Label(accountWindow,font=('Helvetica',12),text=f"Games:{games}").pack()
        Label(accountWindow,font=('Helvetica',12),text=f"Wins:{wins}").pack()
        Label(accountWindow,font=('Helvetica',12),text=f"Losses:{losses}\n").pack()
        Button(accountWindow,text="Load Games",font=('Helvetica',12),command=self.LoadGamesWindow,height=2,width=25).pack()
        Label(accountWindow,text=" ",font=('Helvetica',12)).pack()
        Button(accountWindow,font=('Helvetica',12),text="Quit",height=2,width=15,command=accountWindow.destroy).pack()


    def LoadGamesWindow(self):
        LoadGamesWindow=Toplevel(self._root)
        LoadGamesWindow.title("Scrabble - Account - Load Games")
        Label(LoadGamesWindow,font=('Helvetica',30),text="Load Games").pack()       
        frameContainer=Frame(LoadGamesWindow)
        canvasCointainer = Canvas(frameContainer)
        frame2=Frame(canvasCointainer)

        scrollbar= Scrollbar(frameContainer,orient="vertical",command=canvasCointainer.yview)
        canvasCointainer.create_window((0,0),window=frame2,anchor="nw")

        gameList=["a","b","c","d","e","f","g","h","i","j","k","l","m"]
        for i in range(len(gameList)):
            Button(frame2,text=gameList[i],width=50,height=1,font=('Helvetica',12)).pack(pady=5)
        
        frame2.update()
        canvasCointainer.configure(yscrollcommand=scrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvasCointainer.pack(side=LEFT)

        scrollbar.pack(side=RIGHT,fill=Y)
        frameContainer.pack()

        Button(LoadGamesWindow,text="Quit",font=('Helvetica',12),width=15,height=1,command=LoadGamesWindow.destroy).pack(pady=20)





    def main(self):


        self._root.title("Scrabble - Main Menu")
        frame = Frame(self._root)
        frame.pack()



        Button(frame,text='Play Game',width = 40,height =3,command=self.SelectLanguage).pack(fill=X)
        Button(frame,text='Account',width = 40,height =3,command = self.AccountCheck).pack(fill=X)
        Button(frame,text='Create Acount',width = 40,height =3,command=self.CreateAccountWindow).pack(fill=X)
        Button(frame,text='Login',width = 40,height =3, command=self.login).pack(fill=X)
        Button(frame,text='Help',width = 40,height =3).pack(fill=X)
        Button(frame,text='Quit',command=self._root.quit,width = 40,height =3).pack(fill=X)
        self._root.mainloop()

    def PlayGame(self):
        pass


gui = GUI()