from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class PostsDB(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    body = Column(String)
    creator = relationship('UsersDB', back_populates='Posts')


class UsersDB(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    Posts = relationship('PostsDB', back_populates='creator')
