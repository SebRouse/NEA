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
        self._Dawg = None
        self._currLanguage=None


    def CreateDawg(self,filename):
        self._Dawg=Dawg()
        file1 = open(filename,'r')
        lines = file1.readlines()
        for line in lines:
            self._Dawg.insert(line)
    

    def search(self,word):
        match =self._Dawg.search(word)
        return match



class English(Dictionary):
    def __init__(self):
        self._bag=[]
        for i in range(12):
            self._bag.append("E")
        for i in range(9):
            self._bag.append("I")
            self._bag.append("A")
        for i in range(8):
            self._bag.append("O")
        for i in range(6):
            self._bag.append("N")
            self._bag.append("R")
            self._bag.append("T")
        


class Player:
    def __init__(self):
        self._points = 0
        self._rack = 0
    






    

        



        