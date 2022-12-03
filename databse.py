import sqlite3


class Databse():

   con = sqlite3.connect("game.db")
   cur = con.cursor()
   res = cur.execute("""CREATE TABLE IF NOT EXISTS Players (
      Username VARCHAR(255) PRIMARY KEY NOT NULL,
      Password VARCHAR(255) NOT NULL,
      NumGames INT,
      Wins INT,
      Losses INT,
   );""")
   res = cur.execute("""CREATE TABLE IF NOT EXISTS Games(
      GameID INT PRIMARY KEY,
      TurnNo INT,
      Board VARCHAR(255),
      Scores VARCHAR(255),
      Bag VARCHAR(255),
      Language VARCHAR(255)
      );""")
   res= cur.executemany("""CREATE TABLE IF NOT EXISTS GamesPlayed(
      Id INT PRIMARY KEY,
      Username VARCHAR(255),
      GameID INT
      );""")
   con.commit()


