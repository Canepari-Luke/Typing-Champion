from fastapi import APIRouter, Body, Depends
from dotenv import load_dotenv
from models.database import ConnectDatabase
from models.user import CreateUser
import os
import hashlib
import logging

#Create a new APIRouter instance
Router = APIRouter()
load_dotenv()

#Get the environment variables
HOST = os.getenv("HOST")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
DATABASE = os.getenv("DATABASE")

#Check if the environment variables are set
if not all([HOST, USER, PASSWORD, DATABASE]):
    raise ValueError("One or more environment variables are missing")

#Set the logging level to INFO
logging.basicConfig(level=logging.INFO)

#Hash the password  
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

#Connect to DB or throw an error if it fails.
def get_db_connection():
    connection = ConnectDatabase(HOST, USER, PASSWORD, DATABASE).Connection()
    if not connection:
        return {"error": "Cannot connect to database"}
    return connection

#Check if the table exists and create it if it doesn't.
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

#create user via POST method.
@Router.post("/create/")

#collect values from input then parse the data so it can be used in the function.
def create_user(user: CreateUser = Body(...), connection_string=Depends(get_db_connection)):
    logging.info("Parsed User Data: %s", user)

    #Create a cursor object to execute SQL queries
    cursor = connection_string.cursor()
    
    try:
        # Check if the table exists and create it if it doesn't
        check_and_create_table(cursor)
        
        # Hash the password
        hashed_password = hash_password(user.Password)
        cursor.execute(
            "INSERT INTO user (Username, FirstName, Lastname, Password) VALUES (%s, %s, %s, %s)",
            (user.Username, user.FirstName, user.Lastname, hashed_password)
        )
        # Commit the transaction
        connection_string.commit()

        # Return a success message
        return {"message": "User created successfully"}
    
    # Catch any exceptions and log them
    except Exception as e:
        connection_string.rollback()
        logging.error("Error creating user: %s", e)
        return {"Status": "error", "message": str(e)}
    
    # Close the cursor and connection
    finally:
        cursor.close()
        connection_string.close()