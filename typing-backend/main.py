from fastapi import FastAPI
from routes.user import Router as User

server = FastAPI()

server.include_router(User, prefix="/api")

@server.get("/")
def Root():
    return {"message":"Entry Point"}