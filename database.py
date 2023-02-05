import sqlite3
import hashlib
from Hashing import Sha256


class Account():
   def __init__(self):
      self._Account = None
      self._database= Database()



   def Login(self,Username,Password):
      result = self._database.Login(Username,Password)
      if result==False:
         return False
      else:
         self._Account= result[0][0]
         return True

   def getAccount(self):
      return self._Account

   def CreateAccount(self,username,password):
      result= self._database.CreateAccount(username,password)
      print(result)
      return result


   def GetWinLoss(self):
      result = self._database.GetWinLoss(self._Account)
      return result

   def SaveGame(self,TurnNo,Board,Scores,Bag,Langauge,rackP1,rackP2):
      self._database.saveGame(self._Account,TurnNo,Board,Scores,Bag,Langauge,rackP1,rackP2)

   def UpdateWin(self):
      self._database.updateWin(self._Account)

   def UpdateLoss(self):
      self._database.updateLoss(self._Account)

   def SaveGame(self,TurnNo,Board,Scores,Bag,Language,rack1,rack2):
      self._database.saveGame(self._Account,TurnNo,Board,Scores,Bag,Language,rack1,rack2)

   def LoadGame(self,GameID):
      return self._database.loadGame(GameID)

   def GetGames(self):
      return self._database.GetGames(self._Account)






class Database():
   
   def __init__(self):
      self._Sha256 = Sha256()

      self.CreateTables()


   def CreateTables(self):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      c.execute("""CREATE TABLE IF NOT EXISTS Players (
      Username VARCHAR(255) PRIMARY KEY,
      Password VARCHAR(255),
      NumGames INT,Wins INT,
      Losses INT)""")
      c.execute("""CREATE TABLE IF NOT EXISTS Games(
         GameID INTEGER PRIMARY KEY AUTOINCREMENT,
         TurnNo INT,
         Board VARCHAR(255),
         Scores VARCHAR(255),
         Bag VARCHAR(255),
         Language VARCHAR(255),
         RackP1 VARCHAR(255),
         RackP2 VARCHAR(255));""")
      c.execute("""CREATE TABLE IF NOT EXISTS GamesPlayed(
        Username VARCHAR(255) ,
        GameID INT ,
        PRIMARY KEY(Username,GameID),
        FOREIGN KEY (Username) 
           REFERENCES Players (Username),
        FOREIGN KEY(GameID)
            REFERENCES Games (GameID)
         );""")
      con.commit()


   def CreateAccount(self,username,password):
      pHashed= self.PasswordHash(password)

      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()

      c.execute("SELECT Username FROM Players WHERE Username = ?",(username,))
      result = c.fetchall()
   
      if len(result) == 0:
         c.execute("INSERT INTO Players(Username,Password,NumGames,Wins,Losses) VALUES (?,?,0,0,0)",(username,pHashed))
         con.commit()
         return True
      else:
         return False


   def PasswordHash(self,password:str):
      p=self._Sha256.HashAndDigest(password)
      return p

   def Login(self,username:str,password:str):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      pHashed= self.PasswordHash(password)
      c.execute("SELECT Username FROM Players WHERE Username = ? AND Password = ? ",(username,pHashed))
      result = c.fetchall()
      if len(result) == 0:
         return False
      else:
         return result

   def updateWin(self,username:str):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      c.execute("UPDATE players SET Wins = Wins + 1 WHERE Username = ? ",(username,))
      c.execute("UPDATE players SET NumGames = NumGames + 1 WHERE Username = ? ",(username,))
      con.commit()


      
   def updateLoss(self,username:str):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      c.execute("UPDATE players SET NumGames = NumGames + 1 WHERE Username = ? ",(username,))
      c.execute("UPDATE players SET Losses = Losses + 1 WHERE Username = ? ",(username,))
      con.commit()     

   def saveGame(self,username,TurnNo,Board,Scores,Bag,Language,RackP1,RackP2):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      c.execute("INSERT INTO Games (TurnNo,Board,Scores,Bag,Language,RackP1,RackP2) VALUES (?,?,?,?,?,?,?)",(TurnNo,Board,Scores,Bag,Language,RackP1,RackP2))
      c.execute("SELECT last_insert_rowid()")
      GameID =c.fetchall()[0][0]
      print(GameID)
      c.execute("INSERT INTO GamesPlayed (Username,GameId) VALUES (?,?)",(username,GameID))
      con.commit()

   def loadGame(self,GameID):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      c.execute("SELECT TurnNo,Board,Scores,Bag,Language,RackP1,RackP2 FROM Games WHERE GameID = ?",(GameID,))
      result = c.fetchall()
      return result

   def GetWinLoss(self,username):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      c.execute("SELECT NumGames,Wins,Losses FROM Players WHERE Username = ?",(username,))
      result = c.fetchall()
      return result

   def GetGames(self,username):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      c.execute("""SELECT Games.GameID, Games.TurnNo,Games.Scores, Games.Language
      FROM Games
      INNER JOIN GamesPlayed ON GamesPlayed.GameID = Games.GameID
      WHERE GamesPlayed.Username = ?""",(username,))  
      result = c.fetchall()
      return result  




