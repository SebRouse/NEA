
from genericpath import exists
from Languages import Dictionary
import random

class Game:

    def __init__ (self):
        self._board = [[" "]*15 for y in range (15)]
        self._boardPoints= [["TWS",None,None,"DLS",None,None,None,"TWS",None,None,None,"DLS",None,None,"TWS"],
        [None,"DWS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"DWS",None],
        [None,None,"DWS",None,None,None,"DLS",None,"DLS",None,None,None,"DWS",None,None],
        ["DLS",None,None,"DWS",None,None,None,"DLS",None,None,None,"DWS",None,None,"DLS"],
        [None,None,None,None,"DWS",None,None,None,None,None,"DWS",None,None,None,None],
        [None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None],
        [None,None,"DLS",None,None,None,"DLS",None,"DLS",None,None,None,"DLS",None,None],
        ["TWS",None,None,"DLS",None,None,None,"DWS",None,None,None,"DLS",None,None,"TWS"],
        [None,None,"DLS",None,None,None,"DLS",None,"DLS",None,None,None,"DLS",None,None],
        [None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None],
        [None,None,None,None,"DWS",None,None,None,None,None,"DWS",None,None,None,None],
        ["DLS",None,None,"DWS",None,None,None,"DLS",None,None,None,"DWS",None,None,"DLS"],
        [None,None,"DWS",None,None,None,"DLS",None,"DLS",None,None,None,"DWS",None,None],
        [None,"DWS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"DWS",None],
        ["TWS",None,None,"DLS",None,None,None,"TWS",None,None,None,"DLS",None,None,"TWS"]]
        self._numPlayers=0
        self._NoOfTurn=0
        self._pTurn=0
        self._dict= Dictionary()
        self._currBag =None
        self.players=[]

        self.formedWords=[]
        self._pointsDict ={}


    def updateLanguage(self,n):
        self._dict.updateLanguage(n)
        self._currBag= self._dict.getBag()
        self._pointsDict=self._dict.getPointsDict()

    def incrementTurn(self):
        self._NoOfTurn+=1
        self._pTurn = self._NoOfTurn % self._numPlayers

    def ChangeNumPlayers(self,numPlayers):
        self._numPlayers= numPlayers
    
    def getTurnNo(self):
        return(self._NoOfTurn)
    
    def getPTurn(self):
        return(self._pTurn)

    def getBoard(self):
        return self._board

    def playTurn(self):
        pass

    def getNumPlayers(self):
        return self._numPlayers

    def addPlayers(self,numPlayers):
        for i in range(numPlayers):
            self.players.append(Player())
        self._numPlayers= numPlayers

    def updatePlayerRack(self,n):
        rack = self.players[n].displayRack()
        for i in range(7-len(rack)):
            if self._currBag:
                x=random.randint(0,len(self._currBag)-1)
                rack.append(self._currBag[x])
                self._currBag.pop(x)
            else:
                break
        self.players[n].updateRack(rack)
        
    def isGameOver(self):
        if not self._currBag and not self.players.displayRack():
            self.deductPoints()
            return True
        else:
            return False


    def validateTurn(self,currMoves):

        pRack =self.players[self._pTurn].displayRack()


        playedCentre = False
        for i in range (len(currMoves)):

            if currMoves[i][0] not in pRack:
                if "blank" not in pRack:
                    print("Letters not in rack")
                    return False
                else:
                    pRack.remove("blank")
            else:
                pRack.remove(currMoves[i][0])

            if currMoves[i][1] >= 15 or currMoves[i][2] >= 15 or currMoves[i][1]<0 or currMoves[i][2] < 0:
                print("Coordinates out of range")
                return False

            if currMoves[i][1] ==7 and currMoves[i][2] == 7:
                playedCentre = True
        
        if self._NoOfTurn == 0:
            if not playedCentre:
                return False
        

        vert= True
        horz = True
        for i in range(len(currMoves)-1):
            if horz and currMoves[i][1] == currMoves[i+1][1]:
                vert = False
            elif vert and currMoves[i][2] == currMoves[i+1][2]:
                horz = False
            else:
                print("Coordinates not in row")
                return False

        boardCopy = self._board

        for i in range(len(currMoves)):
            
            if boardCopy[currMoves[i][1]][currMoves[i][2]] != " ":
                print("A piece already occupies that square")

                return False
            
            boardCopy[currMoves[i][1]][currMoves[i][2]] = currMoves[i][0]


        match =1
        count = 1
        if vert == True:
            while True:
                horizontalValue= currMoves[0][2]
                if currMoves[0][1] + count >= 15 or boardCopy[currMoves[0][1]+count][horizontalValue] == None:
                    break
                
                for i in range(len(currMoves)):
                    if currMoves[0][1]+count == currMoves[i][1]:
                        match += 1
                    
                count += 1

            count = 1
            while True:
                horizontalValue= currMoves[i][2]
                if currMoves[0][1] - count <0 or boardCopy[currMoves[0][1]-count][horizontalValue] == None:
                    break
                
                for i in range(len(currMoves)):
                    if currMoves[0][1]-count == currMoves[i][1]:
                        match += 1
                    
                count += 1          

        elif horz == True:
            while True:
                verticalValue= currMoves[0][1]
                if currMoves[0][2] + count >= 15 or boardCopy[verticalValue][currMoves[0][2]+count] == None:
                    break
                
                for i in range(len(currMoves)):
                    if currMoves[0][2]+count == currMoves[i][2]:
                        match += 1
                    
                count += 1
            count =1
            while True:
                verticalValue= currMoves[0][1]
                if currMoves[0][2] - count <0 or boardCopy[verticalValue][currMoves[0][2]-count] == None:
                    break
                
                for i in range(len(currMoves)):
                    if currMoves[0][2]-count == currMoves[i][2]:
                        match += 1
                    
                count += 1   

        if match != len(currMoves):
            print("Letters not connected")
            return False

        word = ""
        if vert == True:
            for i in range(currMoves[0][1],15):
                if boardCopy[i][currMoves[0][2]] == None:
                    break
                else:
                    word = word + boardCopy[i][currMoves[0][2]]
            for i in range(currMoves[0][1]-1,-1,-1):
                if boardCopy[i][currMoves[0][2]] == None:
                    break
                else:
                    word =  boardCopy[i][currMoves[0][2]] + word

            if self._dict.search(word) == False:
                print("Flag 1")
                print(word)
                return False

            for i in range(len(currMoves)):
                word =""
                for j in range(currMoves[i][2],15):
                    if boardCopy[currMoves[i][1]][j] == " ":
                        break
                    else:
                        word = word + boardCopy[currMoves[i][1]][j]
                for j in range(currMoves[i][2]-1,-1,-1):
                    if boardCopy[currMoves[i][1]][j] == " ":
                        break
                    else:
                        word = boardCopy[ currMoves[i][1] ][j] + word    

                if len(word) > 1:
                    if self._dict.search(word)==False:
                        print("Flag 2")
                        print(word)
                        return False

        elif horz == True:
            for i in range(currMoves[0][2],15):
                if boardCopy[currMoves[0][1]][i] == " ":
                    break
                else:
                    word = word + boardCopy[currMoves[0][1]][i]
            for i in range(currMoves[0][2]-1,-1,-1):
                if boardCopy[currMoves[0][1]][i] == " ":
                    break
                else:
                    word = boardCopy[currMoves[0][1]][i] + word 

            if self._dict.search(word) == False:
                print(word)
                print("Flag 3")
                return False

            for i in range(len(currMoves)):
                word = ""
                for j in range(currMoves[i][1],15):
                    if boardCopy[j][currMoves[i][2]] == " ":
                        break
                    else:
                        word = word + boardCopy[j][currMoves[i][2]]
                for j in range(currMoves[i][1]-1,-1,-1):
                    if boardCopy[j][ currMoves[i][2] ] == " ":
                        break
                    else:
                        word =  boardCopy[j][currMoves[i][2]] + word  
                if len(word)> 1:
                    if self._dict.search(word) == False:
                        print("Flag 4")
                    
                        print(word)
                        return False

        self._board = boardCopy

        return True   



    def calculatePoints(self,currMoves):
        if len(currMoves)==1:
            vert = True
            horz = False
        elif currMoves[0][1] == currMoves[1][1]:
            vert = True
            horz = False
        else:
            vert = False
            horz = True

        totalPoints=0

        if vert == True:
            vMultiplier = 1 
            
            for i in range(len(currMoves)):
                wordPoints = 0
                hMultiplier = 1
                lMultiplier =1
                match self._boardPoints[currMoves[i][1]][currMoves[i][2]] :
                    case "TWS":
                        hMultiplier = hMultiplier*3
                        vMultiplier= vMultiplier*3
                    case "DWS":
                        hMultiplier =  hMultiplier*2
                        vMultiplier = vMultiplier*2
                    case "TLS":
                        lMultiplier = 3
                    case "DLS":
                        lMultiplier = 2
                wordPoints += self._pointsDict[ self._board [currMoves[i][1]] [currMoves[i][2]] ] *lMultiplier             
                           
                for j in range(currMoves[i][2]+1,15):
                    if self._board[currMoves[i][1]][j] == " ":
                        break
                    elif self._board[currMoves[i][1]][j].islower():
                        pass
                    else:
                        wordPoints+=self._pointsDict[ self._board[currMoves[i][1]][j]]
    

                for j in range(currMoves[i][2]-1,-1,-1):
                    if self._board[currMoves[i][1]][j] == " ":
                        break
                    elif self._board[currMoves[i][1]][j].islower():
                        pass
                    else:
                        wordPoints+=self._pointsDict[ self._board[currMoves[i][1]][j]]
                wordPoints=wordPoints*hMultiplier
                totalPoints+=wordPoints

            wordPoints = 0
            for i in range(currMoves[0][1],15):
            
                lMultiplier = 1
                if self._board[i][currMoves[0][2]] == " ":
                    break
                elif self._board[i][currMoves[0][2]].islower():
                    pass     
                else:
                    for j in range(len(currMoves)):
                        if currMoves[j][1]==i:
                            match self._boardPoints[[i][currMoves[0][2]]] :
                                case "TLS":
                                    lMultiplier = 3
                                case "DLS":
                                    lMultiplier = 2
                    wordPoints+=self._pointsDict[self._board[currMoves[i][1]][currMoves[0][2]]]*lMultiplier
                    
            for i in range(currMoves[0][1]-1,-1,-1):
                if self._board[i][currMoves[0][2]] == " ":
                    break
                elif self._board[i][currMoves[0][2]].islower():
                    pass              
                else:
                    for j in range(len(currMoves)):
                        if currMoves[j][1]==i:
                            match self._boardPoints[[i][currMoves[0][2]]] :
                                case "TLS":
                                    lMultiplier = 3
                                case "DLS":
                                    lMultiplier = 2
                    wordPoints+=self._pointsDict[self._board[currMoves[i][1]][currMoves[0][2]]]*lMultiplier
            wordPoints=wordPoints*vMultiplier
            totalPoints+=wordPoints


        if horz == True:
            hMultiplier =1

            for i in range(len(currMoves)):
                wordPoints=0
                vMultiplier=1
                match self._boardPoints[currMoves[i][1]][currMoves[i][2]] :
                    case "TWS":
                        vMultiplier = vMultiplier*3
                        hMultiplier= hMultiplier*3
                    case "DWS":
                        vMultiplier =  vMultiplier*2
                        hMultiplier = hMultiplier*2
                    case "TLS":
                        lMultiplier = 3
                    case "DLS":
                        lMultiplier = 2
                if not self._board[currMoves[i][1]][currMoves[i][2]].islower():
                    wordPoints += self._pointsDict[ self._board [currMoves[i][1]] [currMoves[i][2]] ] *lMultiplier


                for j in range(currMoves[i][1],15):
                    if self._board[j][currMoves[i][2]] == " ":
                        break
                    elif self._board[j][ currMoves[i][2] ].islower():
                        pass
                    else:
                        wordPoints+=self._pointsDict[self._board[j][currMoves[i][2]]]
                for j in range(currMoves[i][1]-1,-1,-1):
                    if self._board[j][ currMoves[i][2] ] == " ":
                        break
                    elif self._board[j][ currMoves[i][2] ].islower():
                        pass
                    else:
                        wordPoints+=self._pointsDict[self._board[j][currMoves[i][2]]]
                wordPoints =wordPoints*vMultiplier
                totalPoints+=wordPoints

            wordPoints = 0
            lMultiplier=1
            for i in range(currMoves[0][2],15):

                if self._board[currMoves[0][1]][i] == " ":
                    break
                elif self._board[currMoves[0][1]][i].islower():
                    pass
                else:
                    for j in range(len(currMoves)):
                        if currMoves[j][2]==i:
                            match self._boardPoints[currMoves[0][1]][i] :
                                case "TLS":
                                    lMultiplier = 3
                                case "DLS":
                                    lMultiplier = 2
                    wordPoints += self._pointsDict[self._board[currMoves[0][1]][i]]*lMultiplier
            for i in range(currMoves[0][2]-1,-1,-1):
                if self._board[currMoves[0][1]][i] == " ":
                    break
                elif self._board[currMoves[0][1]][i].islower():
                    pass
                else:
                    for j in range(len(currMoves)):
                        if currMoves[j][2]==i:
                            match self._boardPoints[currMoves[0][1]][i] :
                                case "TLS":
                                    lMultiplier = 3
                                case "DLS":
                                    lMultiplier = 2
                    wordPoints += self._pointsDict[self._board[currMoves[0][1]][i]]*lMultiplier
            wordPoints=wordPoints*hMultiplier
            totalPoints+=wordPoints
        if len(currMoves)==7:
            totalPoints+=50
        self.player[self._pTurn].updatePoints(totalPoints)

        return totalPoints

    def findWinner(self):
        Max = 0
        index= None
        flag = False
        for i in range (self._numPlayers):
            if self.players[i].getPoints() > Max:
                Max = self.players[i].getPoints()
                index == i
            elif self.players[i].getPoints() ==Max:
                flag = True
        
        if flag:
            Max = 0
            index = None
            for i in range (self._numPlayers):
                if self.players[i].getPreEndPoints() > Max:
                    Max = self.players[i].getPreEndPoints()
                    index == i

        return index 




    def deductPoints(self):
        points = 0
        index = None
        for i in range (self._numPlayers):
            self.players[i].updatePreEndPoints(self.players[i].getPoints())
            if len(self.players[i].displayRack()) == 0:
                index = i
            else:
                playerPoints = 0
                for j in self.players[i].displayRack():
                    playerPoints += self._pointsDict[j]
                    
                points += playerPoints

                self.players[i].updatePoints (-playerPoints)

        self.players[index].updatePoints(points)




    def printBoard(self):

        x = "   "
        for i in range(10):
            x +=(" "+str(i)+"   ")
        for i in range (10,15):
            x +=(" "+str(i)+"  ")

        print(x)
        for i in range(10):
            print(str(i)+" "+str(self._board[i]))
        for i in range(10,15):
            print(str(i)+str(self._board[i]))    


    def createDatabaseTable():
        if not exists("./scrabble.db"):    
            pass
 
        

    

        


class Player:
    def __init__(self):
        self._points = 0
        self._rack = []
        self._preEndPoints = 0

    def updateRack(self,NewRack):
        self._rack=NewRack

    def displayRack(self):
        return self._rack

    def updatePoints(self,points):
        self._points+= points

    def getPoints(self):
        return self._points

    def updatePreEndPoints(self,points):
        self._preEndPoints+= points

    def getPreEndPoints(self):
        return self._preEndPoints
    
    






    

        



        