from fastapi import FastAPI
from routes.user import Router as User
from routes.create import Router as Create
from fastapi.middleware.cors import CORSMiddleware

server = FastAPI()

server.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

server.include_router(User, prefix="/api")
server.include_router(Create, prefix="/api")

@server.get("/")
def Root():
    return {"message":"Entry Point"}