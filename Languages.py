from DAWG import Dawg
from DAWG import DawgNode
from pathlib import Path


class Dictionary:
    def __init__(self):
        self._Dawg=None
        self._languages={"English":English(),"Spanish":Spanish()}
        self._pointsDict=None
        self._bag=[]


    def CreateDawg(self,filename:str):
        self._Dawg=Dawg()
        file1 = open(filename,"r")
        lines = file1.readlines()
        for line in lines:
            self._Dawg.insert(str(line).strip().upper())
    

    def search(self,word :str):
        match =self._Dawg.search(word.upper())
        return match

    def updateLanguage(self,l:str):
        self._bag = self._languages[l].returnBag()
        self._pointsDict = self._languages[l].returnPointsDict()
        self.CreateDawg(self._languages[l].returnFilename())

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
                self._bag.append("I")
                self._bag.append("A")
            if i<8:
                self._bag.append("O")
            if i<6:
                self._bag.append("N")
                self._bag.append("R")
                self._bag.append("T")
            if i <4:
                self._bag.append("D")
                self._bag.append("L")
                self._bag.append("S")
                self._bag.append("U")
            if i <3:
                self._bag.append("G")
            if i<2:
                self._bag.append("B")
                self._bag.append("C")
                self._bag.append("F")
                self._bag.append("H")
                self._bag.append("M")
                self._bag.append("P")
                self._bag.append("V")
                self._bag.append("W")
                self._bag.append("Y")
                self._bag.append("blank")
            if i<1:
                self._bag.append("J");self._bag.append("K");self._bag.append("Q");self._bag.append("X");self._bag.append("Z")
        self._pointsDict = {"blank":0,"A":1,"E":1,"I":1,"L":1,"N":1,"O":1,"S":1,"T":1,"U":1,"D":2,"G":2,"B":3,"C":3,"M":3,"P":3,"F":4,"H":4,"V":4,"W":4,"Y":4,"K":5,"J":8,"X":8,"Q":10,"Z":10,"R":2}

        self._filename= "English.txt"
    
    def returnBag(self):
        return self._bag
    
    def returnPointsDict(self):
        return self._pointsDict  

    def returnFilename(self):
        return self._filename


class Spanish:
    def __init__(self):
        self._bag=[]
        for i in range(12):
            self._bag.append("A")
            self._bag.append("E")
            if i < 9:
                self._bag.append("O")
            if i <6:
                self._bag.append("S")
                self._bag.append("I")
            if i <5:
                self._bag.append("D")
                self._bag.append("U")
                self._bag.append("N")
                self._bag.append("R")
            if i <4:
                self._bag.append("C")
                self._bag.append("L")
                self._bag.append("T")
            if i<2:
                self._bag.append("B")
                self._bag.append("G")
                self._bag.append("H")
                self._bag.append("M")
                self._bag.append("P")
                self._bag.append("blank")
            if i<1:
                self._bag.append("CH")
                self._bag.append("F")
                self._bag.append("J")
                self._bag.append("LL")
                self._bag.append("Ñ")
                self._bag.append("Q")
                self._bag.append("RR")
                self._bag.append("V")
                self._bag.append("X")
                self._bag.append("Y")
                self._bag.append("Z")

        self._pointsDict = {"blank":0,"Z":10,"Y":4,"X":8,"V":4,"U":1,"T":1,"S":1,"RR":8,"R":1,"Q":5,"P":3,"O":1,"Ñ":8,"N":1,"M":3,"LL":8,"L":1,"J":8,"I":1,"H":4,"G":2,"F":4,"E":1,"D":2,"CH":5,"C":3,"B":3,"A":1}

        self._filename="Spanish.txt"

        self.__TrimSpanishDict()




    def returnBag(self):
        return self._bag
    
    def returnPointsDict(self):
        return self._pointsDict  

    def returnFilename(self):
        return self._filename

    def __TrimSpanishDict(self):

        path = Path('./Spanish.txt')

        if path.is_file():
            pass

        else:
            file=open("Spanish Untrimmed.txt","r",encoding="utf-8",errors="ignore")
            spanish = open("Spanish.txt","a")
            lines=file.readlines()
            for i in range(1,len(lines)):
                flag = False
                line =""
                for j in range( len(lines[i])):

                    char =lines[i][j]
                    
                    if char == "ñ":
                        print("Check")
                        flag=True

                    if char== "á":
                        char= "a"
                    elif char == "é":
                        char="e"
                    elif char ==  "í":
                        char="i"
                    elif char ==  "ó":
                        char="o"
                    elif char ==  "ú":
                        char="u"

                
                    line+=char

                if flag:
                    print(line)
                    print(line.upper())
                spanish.write(f"{line.upper()}")


