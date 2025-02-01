from fastapi import FastAPI
from routes.user import Router as User
from routes.create import Router as Create

server = FastAPI()

server.include_router(User, prefix="/api")
server.include_router(Create, prefix="/api")

@server.get("/")
def Root():
    return {"message":"Entry Point"}