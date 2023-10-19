from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)



class Demo(Base):
    __tablename__ = "demos"
    
    id = Column(Integer, primary_key=True, index=True)
    text=Column(String)
    description = Column(String)

