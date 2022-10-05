from DAWG import Dawg
from DAWG import DawgNode


class Dictionary:
    def __init__(self):
        self._Dawg=None
        self._languages[English()]
        self._pointsDict=None
        self._bag=None


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

    def getBag(self):
        return self._bag
    
    def getPointsDict(self):
        return self._pointsDict




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




        self._filename= "English.txt"
    
    def returnBag(self):
        return self._bag
    
    def returnPointsDict(self):
        return self._pointsDict

    def returnFilename(self):
        return self._filename