from fastapi import APIRouter
from dotenv import load_dotenv
from models.database import ConnectDatabase
import os

Router = APIRouter()
load_dotenv()

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")
print(HOST, USER, PASSWORD, DATABASE)


@Router.get("/users/")
async def GetAllUsers():
    try:
        ConnectionString = ConnectDatabase(HOST, USER, PASSWORD, DATABASE).Connection()
        Cursor = ConnectionString.cursor(dictionary=True)
        Cursor.execute("SELECT * FROM User")
        Users = Cursor.fetchall()
        return Users
    except:
        return {"error":"Cannot Connect to Database"}

@Router.get("/user/{username}")
async def GetSingleUser(username: str):
    try:
        ConnectionString = ConnectDatabase(HOST, USER, PASSWORD, DATABASE).Connection()
        try:
            Cursor = ConnectionString.cursor(dictionary=True)
            Cursor.execute(f"SELECT CONCAT(Firstname,' ',Lastname) AS Name FROM User WHERE Username = {username}")
            User = Cursor.fetchone()
            Cursor.execute(f"SELECT G.WordPerMinute, G.Accuracy, G.Level, G.LivesLeft FROM User U INNER JOIN Game G ON U.Id = G.User_Id WHERE U.Username = {username}")
            UserDetails = Cursor.fetchall()
            return User, UserDetails
        except:
            return {"Error":f"Cannot Find {username}"}
    except:
        return {"Error":"Cannot connect to Database"}

@Router.get("/scores")
async def GetAllScores():
    try:
        ConnectionString = ConnectDatabase(HOST, USER, PASSWORD, DATABASE).Connection()
        try:
            Cursor = ConnectionString.cursor(dictionary=True)
            Cursor.execute("SELECT CONCAT(U.Firstname, ' ', U.Lastname) AS Name, G.WordPerMinute, G.Accuracy, G.Level, G.LivesLeft FROM User U INNER JOIN Game G ON U.Id = G.User_Id ORDER BY G.Level DESC")
            Scores = Cursor.fetchall()
            return Scores
        except:
            return {"Error":"Cannot find scores"}
    except:
        return {"Error":"Cannot connect to Database"}
