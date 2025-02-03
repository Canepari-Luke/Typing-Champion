from fastapi import APIRouter, Body, Depends
from dotenv import load_dotenv
from models.database import ConnectDatabase
from models.user import CreateUser
import os
import hashlib
import logging

Router = APIRouter()
load_dotenv()

HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")

if not all([HOST, USER, PASSWORD, DATABASE]):
    raise ValueError("One or more environment variables are missing")

logging.basicConfig(level=logging.INFO)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def get_db_connection():
    connection = ConnectDatabase(HOST, USER, PASSWORD, DATABASE).Connection()
    if not connection:
        return {"error": "Cannot connect to database"}
    return connection

def check_and_create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Username VARCHAR(255) NOT NULL,
            FirstName VARCHAR(255) NOT NULL,
            Lastname VARCHAR(255) NOT NULL,
            Password VARCHAR(255) NOT NULL
        )
    """)

@Router.post("/create/")
def create_user(user: CreateUser = Body(...), connection_string=Depends(get_db_connection)):
    logging.info("Parsed User Data: %s", user)
    
    cursor = connection_string.cursor()
    
    try:
        # Check if the table exists and create it if it doesn't
        check_and_create_table(cursor)
        
        hashed_password = hash_password(user.Password)
        cursor.execute(
            "INSERT INTO users (Username, FirstName, Lastname, Password) VALUES (%s, %s, %s, %s)",
            (user.Username, user.FirstName, user.Lastname, hashed_password)
        )
        connection_string.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        connection_string.rollback()
        logging.error("Error creating user: %s", e)
        return {"Status": "error", "message": str(e)}
    finally:
        cursor.close()
        connection_string.close()