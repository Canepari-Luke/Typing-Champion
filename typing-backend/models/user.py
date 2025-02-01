from pydantic import BaseModel

class CreateUser(BaseModel):
    Username: str
    FirstName: str
    Lastname: str
    Password: str