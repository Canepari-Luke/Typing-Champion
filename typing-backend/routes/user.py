from fastapi import APIRouter
from helper.query import QueryResult
from helper.queries import AllUsers, SingleUser, GameDetailSingle, AllScores
from helper.connection import MakeConnection
Router = APIRouter()


@Router.get("/users/")
async def GetAllUsers():
    try:
        ConnectionString = MakeConnection()
        try:
            Users = QueryResult(ConnectionString, AllUsers, "multiple", None)
            return Users
        except:
            return {"error":"Cannot Find results"}
    except:
        return {"error":"Cannot Connect to Database"}

@Router.get("/user/{username}")
async def GetSingleUser(username: str):
    try:
        ConnectionString = MakeConnection()
        try:
            User = QueryResult(ConnectionString, SingleUser, 'single', (username,))
            UserDetails = QueryResult(ConnectionString, GameDetailSingle, 'multiple', (username,))
            return User, UserDetails
        except:
            return {"Error":f"Cannot Find {username}"}
    except:
        return {"Error":"Cannot connect to Database"}

@Router.get("/scores")
async def GetAllScores():
    try:
        ConnectionString = MakeConnection()
        try:
            Scores = QueryResult(ConnectionString, AllScores, 'multiple', None)
            return Scores
        except:
            return {"Error":"Cannot find scores"}
    except:
        return {"Error":"Cannot connect to Database"}
