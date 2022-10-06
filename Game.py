
from Languages import Dictionary
import random

class Game:

    def __init__ (self):
        self._board = [[None]*15 for y in range (15)]
        self._boardPoints= [["TWS",None,None,"DLS",None,None,None,"TWS",None,None,None,"DLS",None,None,"TWS"],
        [None,"DWS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"DWS",None],
        [None,None,"DWS",None,None,None,"DLS",None,"DLS",None,None,None,"DWS",None,None],
        ["DLS",None,None,"DWS",None,None,None,"DLS",None,None,None,"DWS",None,None,"DLS"],
        [None,None,None,None,"DWS",None,None,None,None,None,"DWS",None,None,None,None],
        [None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None,None,None,"TLS",None],
        [None,None,"DLS",None,None,None,"DLS",None,"DLS",None,None,None,"DLS",None,None],
        ["TWS",None,None,"DLS",None,None,None,"star",None,None,None,"DLS",None,None,"TWS"],
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
        self.currMoves =[]
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

    def showBoard(self):
        return self._board

    def playTurn(self):
        pass

    def getNumPlayers(self):
        return self._numPlayers

    def addPlayers(self,numPlayers):
        for i in range(numPlayers):
            self._players.append(Player())
        self._numPlayers= numPlayers

    def updatePlayerRack(self,n):
        rack = self.players[n].displayRack()
        for i in range(7-len(rack)):
            if self._currBag:
                x=random.randint(0,len(self._currBag))
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

    def validateTurn(self):
        pass
    
    
    def calculatePoints(self):
        pass


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


    def endTurn(self):
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
    
    






    

        



        