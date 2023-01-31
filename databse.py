import sqlite3
import hashlib



class Account():
   def __init__(self):
      self._Account = None
      self._database= Database()



   def Login(self,Username,Password):
      result = self._database.Login(Username,Password)
      if result==False:
         return False
      else:
         self._Account= result[0]
         return True

   def getAccount(self):
      return self._Account

   def CreateAccount(self,username,password):
      result= self._database.CreateAccount(username,password)
      return result





class Database():
   
   def __init__(self):

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
         Language VARCHAR(255)
         );""")
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


   def PasswordHash(self,password):
      p= hashlib.sha256()
      p.update(password.encode('utf8'))
      pHashed = p.hexdigest()
      return pHashed


   def Login(self,username,password):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      pHashed= self.PasswordHash(password)
      c.execute("SELECT Username FROM Players WHERE Username = ? AND Password = ? ",(username,pHashed))
      result = c.fetchall()
      if len(result) == 0:
         return False
      else:
         return result

   def updateWin(self,username):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      c.execute("UPDATE players SET Wins = Wins + 1 WHERE Username = ? ",(username,))
      c.execute("UPDATE players SET NumGames = NumGames + 1 WHERE Username = ? ",(username,))
      con.commit()


      
   def updateLoss(self,username):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
      c.execute("UPDATE players SET NumGames = NumGames + 1 WHERE Username = ? ",(username,))
      c.execute("UPDATE players SET Losses = Losses + 1 WHERE Username = ? ",(username,))
      con.commit()     

   def saveGame(self):
      pass

   def loadGame(self):
      pass


   def GetGames(self):
      pass

   def GetWinLoss(self,username):
      con = sqlite3.connect("ScrabbleDataBase.db")
      c = con.cursor()
