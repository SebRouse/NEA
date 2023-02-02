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
        self._blank=None
        self._handleBlankWindow = None
        self._blankEntry = None

        



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
        self._LEntryU.pack()
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
        self._CEntryU.pack()
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
        if self._languageWindow:
            return False
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

        self.PlayGame(game)
    
    def PlayGameSpanish(self):
        self._languageWindow.destroy()
        game=Game(self._account)
        game.updateLanguage("Spanish")
        game.addPlayers(2)

        self.PlayGame(game)

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

        gameList=self._account.GetGames()
        for i in range(len(gameList)):
            GameID, TurnNo,Scores, Language =gameList[i]
            Button(frame2,text=f"Game {i}: Scores({Scores}) turn {TurnNo}: {Language}",width=50,height=1,font=('Helvetica',12),command=lambda:self.LoadGame(GameID)).pack(pady=5)
        
        frame2.update()
        canvasCointainer.configure(yscrollcommand=scrollbar.set,scrollregion="0 0 0 %s" % frame2.winfo_height())
        canvasCointainer.pack(side=LEFT)

        scrollbar.pack(side=RIGHT,fill=Y)
        frameContainer.pack()

        Button(LoadGamesWindow,text="Quit",font=('Helvetica',12),width=15,height=1,command=LoadGamesWindow.destroy).pack(pady=20)


    def LoadGame(self,GameId):
        game = Game()
        game.LoadGame(GameId)
        self.PlayGame(game)


    def run(self):


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


    def drawBackround(self,game :Game):


        board_tiles = [[0 for row in range(15)] for col in range(15)]
        block_size = 50
        backboard=game.GetPointsBoard()
        board = game.getBoard()
        buttonColourLight = (229,229,229)
        buttonColourDark=(122, 122, 122)

        font = pygame.font.SysFont(None, 24)
        tileFont =pygame.font.SysFont(None,36)
        titleFont=pygame.font.SysFont(None,48)
        titleFont.set_underline(True)

        self._screen.fill((0,0,0))
        colour=(255,255,255)
        buttonColourLight = (229,229,229)
        
        for row in range(len(board_tiles)):
            for col in range(len(board_tiles[0])):
                if backboard[row][col]=="TWS":
                    txt = font.render("TWS",True,(0,0,0))
                    colour=(40,78,96)

                elif backboard[row][col]=="DWS" and row != 7 and col !=7:
                    colour=(49,155,118) 
                    txt = font.render("DWS",True,(0,0,0))
                    
                elif backboard[row][col]=="DLS":
                    txt = font.render("DLS",True,(0,0,0))
                    colour=(217,89,128)
                elif backboard[row][col] =="TLS":
                    txt = font.render("TLS",True,(0,0,0))
                    colour=(99,170,192)
                elif row==7 and col == 7:
                    txt = font.render("Start",True,(0,0,0))
                    colour =(249,155,69)
                else:
                    txt = font.render("",True,(0,0,0))
                    colour=(255,255,255)

                
                

                rect = pygame.Rect(col*(block_size+1), row*(block_size+1), block_size, block_size)

                pygame.draw.rect(self._screen, colour, rect)

                self._screen.blit(txt,((block_size+1)*col+6,(block_size+1)*row+15))#

                if board[row][col] != " ":
                    pygame.draw.rect(self._screen,buttonColourLight,rect)
                    txt = tileFont.render(board[row][col],True,(0,0,0))
                    self._screen.blit(txt,((block_size+1)*col+15,(block_size+1)*row+15))

        txt = font.render(f"{game.lenBag()} tiles left",True,(255,255,255))
        self._screen.blit(txt,(765,150))
        if self._account.getAccount()!= None:
            img = font.render(f"{self._account.getAccount()} : {game.players[0].getPoints()} points", True, (255,255,255))         
        else:
            img = font.render(f"Player1:{game.players[0].getPoints()} points", True, (255,255,255))
        self._screen.blit(img, (765, 60))
        img=font.render(f'Player2 :{game.players[1].getPoints()} points',True,(255,255,255))
        self._screen.blit(img,(765,90))
        turn = game.getPTurn()+1
        if self._account.getAccount()!= None:
            if turn == 1:
                img = titleFont.render(f"{self._account.getAccount()}'s turn",True,(255,255,255))
            else:
                img = titleFont.render(f"Player{turn}'s turn",True,(255,255,255))                   
        else:  
            img = titleFont.render(f"Player{turn}'s turn",True,(255,255,255))    
            

        self._screen.blit(img,(865,10))





    def PlayGame(self,game:Game):

        
        rack=game.players[game.getPTurn()].displayRack()
        FPS =30
        pygame.init()
        self._screen = pygame.display.set_mode((1200,765))


        movesStack =[]
        board=[[" "]*15 for y in range (15)]
        pygame.display.set_caption("Scrabble - Play Scrabble")
        running = True
        board_tiles = [[0 for row in range(15)] for col in range(15)]
        block_size = 50

        buttonColourLight = (229,229,229)
        buttonColourDark=(122, 122, 122)

        font = pygame.font.SysFont(None, 24)
        tileFont =pygame.font.SysFont(None,36)
        titleFont=pygame.font.SysFont(None,48)
        titleFont.set_underline(True)

        UIrack=[]
        for i in range(len(rack)):
            txt = tileFont.render(rack[i],True,(0,0,0))
            rec = pygame.Rect(765+40+(block_size+1)*i,300,block_size,block_size)
            UIrack.append((txt,rec))
            pygame.draw.rect(self._screen,buttonColourLight,rec)
            self._screen.blit(txt,(765+40+(block_size+1)*i+15,300+10))

        rectangle_draging=False

        self.drawBackround(game)
        clock = pygame.time.Clock()

        TileDragged=None
        startCoords=None

        pygame.display.update()
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    ###drag and drop##
                    for i in range(len(UIrack)):
                        txt,rectangle=UIrack[i]

                        

                        if rectangle.collidepoint(event.pos):
                            
                            TileDragged =i
                            rectangle_draging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = rectangle.x - mouse_x
                            offset_y = rectangle.y - mouse_y

                            startCoords = (rectangle.x,rectangle.y)


                    ####Undo button###
                    if (883+200)>=mousePos[0]>=883 and (440+50)>= mousePos[1]>=440 :
                        if len(movesStack) != 0:
                            rectangle,endCoords,startCoords = movesStack.pop()
                            rectangle.x = startCoords[0]
                            rectangle.y = startCoords[1]

                    ####next turn button#####
                    if (883+200)>=mousePos[0]>=883 and (380+50)>= mousePos[1]>=380:

                        currMoves=[]
                        for i in range(len(rack)):
                            txt,rectangle=UIrack[i]
                            x = rectangle.x //(block_size+1)
                            y= rectangle.y//(block_size+1)
                            if 14>=x>=0 and 14>=y>=0:
                                char = rack[i]
                                if rack[i]=="blank":
                                    self._blank = None
                                    self.HandleBlank()
                                    
                                    char = self._blank.lower()
                                currMoves.append([char,y,x])
                        if game.validateTurn(currMoves):
                            game.calculatePoints(currMoves)

                            game.incrementTurn()
                            if game.isGameOver():
                                i = game.findWinner()
                                if i == 0 and game.user != None:
                                    winner = game.user.getAccount()
                                else:
                                    winner = f"Player {i+1}"
                                running = False
                                

                                
                        

                            rack=game.players[game.getPTurn()].displayRack()
                            UIrack=[]
                            for i in range(len(rack)):
                                char=rack[i]
                                if rack[i]=="blank":
                                    char="_"
                                txt = tileFont.render(char,True,(0,0,0))
                                rec = pygame.Rect(765+40+(block_size+1)*i,300,block_size,block_size)
                                UIrack.append((txt,rec))
                        else:
                            self.invalidTurn()
                    
                    #pass button#
                    if (883+200)>=mousePos[0]>=883 and (500+50)>= mousePos[1]>=500:
                        game.increaseNumPasses()
                        game.incrementTurn()
                        if game.isGameOver():
                            i = game.findWinner()
                            if i == 0 and game.user != None:
                                winner = game.user.getAccount()
                            else:
                                winner = f"Player {i+1}"
                            running = False
                        
                        rack=game.players[game.getPTurn()].displayRack()
                        UIrack=[]
                        for i in range(len(rack)):
                            char=rack[i]
                            if rack[i]=="blank":
                                char="_"
                            txt = tileFont.render(char,True,(0,0,0))
                            rec = pygame.Rect(765+40+(block_size+1)*i,300,block_size,block_size)
                            UIrack.append((txt,rec))
                    
                    ###Save Game and Exit Button####
                    if (883+200)>=mousePos[0]>=883 and (700+50)>= mousePos[1]>=700:
                        game.SaveGame()
                        running = False


                    

                        
                        

                elif event.type == pygame.MOUSEMOTION:
                    if rectangle_draging:
                        txt,rectangle=UIrack[TileDragged]
                        mouse_x, mouse_y = event.pos
                        rectangle.x = mouse_x + offset_x
                        rectangle.y = mouse_y + offset_y  
                
                elif event.type == pygame.MOUSEBUTTONUP:
                    if rectangle_draging:
                    
                        txt,rectangle=UIrack[TileDragged]
                        mouse_x, mouse_y = event.pos
                        if  (mouse_y )//(block_size+1)*(block_size+1) <0 :
                            ycoord=0
                        elif (mouse_y)//(block_size+1)*(block_size+1) >=15*(block_size+1):
                            ycoord = 15*(block_size+1)
                        else:
                            ycoord = (mouse_y)//(block_size+1)*(block_size+1) 
                        
                        if (mouse_x + offset_x)//(block_size+1)*(block_size+1) <0:
                            xcoord =0
                        else:
                            xcoord=(mouse_x )//(block_size+1)*(block_size+1)

                        if 765-block_size>=(mouse_x )//(block_size+1)*(block_size+1)>=0:
                            rectangle.x = xcoord
                            rectangle.y = ycoord
                        else:
                            rectangle.x =765+40+(block_size+1)*TileDragged
                            rectangle.y = 300

                        movesStack.append((rectangle,(rectangle.x,rectangle.y),(startCoords)))

                        
            
                    rectangle_draging = False      

            self.drawBackround(game)
                

            for i in range(len(UIrack)):
                txt,rectangle=UIrack[i]
                
                pygame.draw.rect(self._screen,buttonColourLight,rectangle)
                self._screen.blit(txt,(rectangle.x+15,rectangle.y+10))


            clock.tick(FPS)





            mousePos=pygame.mouse.get_pos()

            ###Next Turn Button###
            if (883+200)>=mousePos[0]>=883 and (380+50)>= mousePos[1]>=380:
                pygame.draw.rect(self._screen,buttonColourDark,[883,380,200, 50])
            else:
                pygame.draw.rect(self._screen,buttonColourLight,[883,380,200, 50])
            txt =font.render('Next Turn',True,(0,0,0))
            self._screen.blit(txt,(945,397))

            ###Undo Button###
            if (883+200)>=mousePos[0]>=883 and (440+50)>= mousePos[1]>=440:
                pygame.draw.rect(self._screen,buttonColourDark,[883,440,200, 50])
            else:
                pygame.draw.rect(self._screen,buttonColourLight,[883,440,200, 50])
            txt = font.render("Undo",True,(0,0,0))
            self._screen.blit(txt,(960,457))


            ###Pass Turn Button###
            if (883+200)>=mousePos[0]>=883 and (500+50)>= mousePos[1]>=500:
                pygame.draw.rect(self._screen,buttonColourDark,[883,500,200, 50])
            else:
                pygame.draw.rect(self._screen,buttonColourLight,[883,500,200, 50])
            txt = font.render("Pass",True,(0,0,0))
            self._screen.blit(txt,(960,517))

            ###Save Game and Exit Button####
            if (883+200)>=mousePos[0]>=883 and (700+50)>= mousePos[1]>=700:
                pygame.draw.rect(self._screen,buttonColourDark,[883,700,200, 50])
            else:
                pygame.draw.rect(self._screen,buttonColourLight,[883,700,200, 50])
            txt= font.render("Save Game & Exit",True,(0,0,0))
            self._screen.blit(txt,(913,717))

            




            pygame.display.update()

        if winner != None:

            self.displayWinner(winner)
        pygame.display.update()

    def HandleBlank(self):
        running = True
        alphabet =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        blocksize=45
        buttonColourLight = (229,229,229)
        buttonColourDark=(122, 122, 122)
        buttons=[]
        tileFont =pygame.font.SysFont(None,36)
        self._screen.fill((0,0,0))
        titleFont =pygame.font.SysFont(None,70)
        txt = titleFont.render("Click the letter that the blank should represent:",True,(255,255,255))
        self._screen.blit(txt,(50,300))
                            
        for i in range(26):
            rect = pygame.Rect((blocksize+1)*i,350,blocksize,blocksize)
            buttons.append(rect)
        while running:
            mousePos=pygame.mouse.get_pos()


            for i in range(26):

                if 350<=mousePos[1]<=(350+blocksize) and (blocksize+1)*i<=mousePos[0]<=(blocksize+1)*(i+1):
                    pygame.draw.rect(self._screen,buttonColourDark,buttons[i])
                else:
                    pygame.draw.rect(self._screen,buttonColourLight,buttons[i])
                txt = tileFont.render(alphabet[i],True,(0,0,0)) 
                self._screen.blit(txt,((blocksize+1)*i+15,350+15))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i in range(26):
                        if 350<=mousePos[1]<=(350+blocksize) and (blocksize+1)*i<=mousePos[0]<=(blocksize+1)*(i+1):
                            self._blank =(alphabet[i])
                            running=False
                
            pygame.display.update()

    def displayWinner(self,winner):
            self._screen.fill((0,0,0))
            font = pygame.font.SysFont(None, 120)
            txt = font.render(f"!!!{winner} wins!!!",True,(255,255,255))
            self._screen.blit(txt,(300,380))



    def invalidTurn(self):
        inavlidTurn=Toplevel(self._root)
        inavlidTurn.title("Scrabble - Play Game - Invalid Turn")
        inavlidTurn.geometry("200x100")
        Label(inavlidTurn,text="Error \n Invalid Turn\n \n").pack()
        Button(inavlidTurn,text="Dismiss",command=inavlidTurn.destroy).pack()


gui = GUI()
gui.run()