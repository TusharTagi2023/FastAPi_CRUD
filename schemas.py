from pydantic import BaseModel
from typing import Optional

class student(BaseModel):
    name:str
    roll:int
    address:Optional[str]

class demo(BaseModel):
    text:str
    description:str


class User(BaseModel):
    username : str
    password : str