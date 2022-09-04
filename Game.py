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


    def incrementTurn(self):
        self._NoOfTurn+=1
        self._pTurn = self._NoOfTurn % self._numPlayers

    def ChangeNumPlayers(self,numPlayers):
        self._numPlayers= numPlayers

    

        



        