
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
            return True
        else:
            return False

    def validateTurn(self):
        pass
    
    def calculatePoints(self):
        points = 0
        for i in range(len(self.currMoves)):
            points += self._pointsDict[self.currMoves[i][0]]
        self.players[self._pTurn].updatePoints(points)

    def findWinner(self):
        pass

    def endTurn(self):
        pass



            
        

        

    

        


class Player:
    def __init__(self):
        self._points = 0
        self._rack = []

    def updateRack(self,NewRack):
        self._rack=NewRack

    def displayRack(self):
        return self._rack

    def updatePoints(self,points):
        self._points+= points

    def displayPoints(self):
        return self._points

    
    






    

        



        