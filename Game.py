from DAWG import Dawg
from DAWG import DawgNode


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
        self._pTurn=1
        self._currBag =None




    def incrementTurn(self):
        self._NoOfTurn+=1
        self._pTurn = self._NoOfTurn % self._numPlayers

    def ChangeNumPlayers(self,numPlayers):
        self._numPlayers= numPlayers

    def playTurn(self):
        pass


class Player:
    def __init__(self):
        self._rack=[]
        self._points=0
        


class Dictionary:
    def __init__(self):
        self._Dawg=None
        self._languages[English()]


    def CreateDawg(self,filename):
        self._Dawg=Dawg()
        file1 = open(filename,'r')
        lines = file1.readlines()
        for line in lines:
            self._Dawg.insert(str(line).strip().upper())
    

    def search(self,word):
        match =self._Dawg.search(word)
        return match

    def updateLanguage(self,i):
        self._bag = self._languages[i].returnBag
        self._pointsDict = self._languages[i].returnPointsDict
        self.CreateDawg(self._languages[i].returnFilename)









class English:
    def __init__(self):
        self._bag=[]
        for i in range(12):
            self._bag.append("E")
            if i<9:
                self._bag.append("I");self._bag.append("A");
            if i<8:
                self._bag.append("O")
            if i<6:
                self._bag.append("N");self._bag.append("R");self._bag.append("T")
            if i <4:
                self._bag.append("D");self._bag.append("L");self._bag.append("S");self._bag.append("U")
            if i <3:
                self._bag.append("G")
            if i<2:
                self._bag.append("B");self._bag.append("C");self._bag.append("F");self._bag.append("H");self._bag.append("M");self._bag.append("P");self._bag.append("V");self._bag.append("W");self._bag.append("Y");self._bag.append("blank")
            if i<1:
                self._bag.append("J");self._bag.append("K");self._bag.append("Q");self._bag.append("X");self._bag.append("Z")
        self._dict = {"blank":0,"A":1,"E":1,"I":1,"L":1,"N":1,"O":1,"S":1,"T":1,"U":1,"D":2,"G":2,"B":3,"C":3,"M":3,"P":3,"F":4,"H":4,"V":4,"W":4,"Y":4,"K":5,"J":8,"X":8,"Q":10,"Z":10}



        self._pointsDict = {}
        self._filename= "English.txt"
    
    def returnBag(self):
        return self._bag
    
    def returnPointsDict(self):
        return self._pointsDict

    def returnFilename(self):
        return self._filename
        


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

    
    






    

        



        