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


@Router.get("/users/")
def GetAllUsers():
    try:
        ConnectionString = ConnectDatabase.Connection(HOST, USER, PASSWORD, DATABASE)
    except:
        return {"error":"Cannot Connect to Database"}


@Router.post("/create/")
def CreateUser():
    ConnectionString = ConnectDatabase(HOST, USER, PASSWORD, DATABASE)
    if not ConnectionString:
        return {"error":"Cannot Connect to Database"}
    Cursor = ConnectionString.cursor()
