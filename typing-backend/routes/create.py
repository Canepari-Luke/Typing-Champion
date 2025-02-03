from fastapi import APIRouter, Body, Depends
from models.user import CreateUser
import logging
from helper.connection import MakeConnection
from helper.query import QueryResult
from helper.queries import AddUser
from helper.Login import hash_password
#Create a new APIRouter instance
Router = APIRouter()

#Set the logging level to INFO
logging.basicConfig(level=logging.INFO)

#create user via POST method.
@Router.post("/create/")

#collect values from input then parse the data so it can be used in the function.
def create_user(user: CreateUser = Body(...)):
    logging.info("Parsed User Data: %s", user)

    #Create a cursor object to execute SQL queries
    try:
        ConnectionString = MakeConnection()
        try:
            User = QueryResult(ConnectionString,AddUser,'create', (user.Username, user.FirstName, user.Lastname, hash_password(user.Password),))
            return User
        except Exception as e:
            return {"Status": "error", "message": str(e)}
    except:
        return {"Error":"Cannot connect to Database"}