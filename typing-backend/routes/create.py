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

@Router.post("/create/")
def CreateUser():
    ConnectionString = ConnectDatabase(HOST, USER, PASSWORD, DATABASE).Connection()
    if not ConnectionString:
        return {"error":"Cannot Connect to Database"}
    Cursor = ConnectionString.cursor()

username:str
firstname:str
lastname:str
password:str