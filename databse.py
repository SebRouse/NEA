import sqlite3


class Databse():

   con = sqlite3.connect("game.db")
   cur = con.cursor()
   res = cur.execute("""CREATE TABLE IF NOT EXISTS Players (
      Username VARCHAR(255) PRIMARY KEY NOT NULL,
      PasswordHash VARCHAR(255) NOT NULL,
      Wins INT,
      Draws INT,
      Losses INT,
      HighestScoringWord VARCHAR(255)
      HighestScore INT
   );""")
   res = cur.execute("""CREATE TABLE IF NOT EXISTS Games(
      GameID INT PRIMARY KEY,
      NumPlayers INT,
      NumHumanPlayers INT,
      NumAIPlayers INT,
      TurnNo INT,
      AIDifficulty VARCHAR(255),
      Board VARCHAR(255),
      Scores VARCHAR(255),
      Ended BOOLEAN,
      Language VARCHAR(255)
      );""")
   res= cur.executemany("""CREATE TABLE IF NOT EXISTS GamesPlayed(
      Username VARCHAR(255),
      GameID INT
      );""")


