from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    isActive = Column(Boolean, default=True)

    goals = relationship("Goal", back_populates="owner")


class Goal(Base):
    __tablename__ = "goals"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    userId = Column(Integer, ForeignKey("users.id"))
    isActive = Column(Boolean, default=True)
    owner = relationship("User", back_populates="goals")

# class Todo(Base):
#     __tablename__ = "todo"

#     id = Column(Integer, primary_key=True, index=True)
#     task = Column(String, index=True)
#     ownerId = Column(Integer, ForeignKey("users.id"))
#     isCompleted = Column(Boolean, default=True)
