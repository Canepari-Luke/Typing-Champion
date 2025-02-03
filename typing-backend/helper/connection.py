import os
from dotenv import load_dotenv
from models.database import ConnectDatabase
def MakeConnection():
    load_dotenv()
    HOST = os.getenv("HOST")
    USER = os.getenv("USER")
    PASSWORD = os.getenv("PASSWORD")
    DATABASE = os.getenv("DATABASE")
    try:
        ConnectionString = ConnectDatabase(HOST, USER, PASSWORD, DATABASE).Connection()
        return ConnectionString
    except:
        return False

