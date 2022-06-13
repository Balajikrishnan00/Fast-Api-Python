from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class DBLogin(Base):
    __tablename__ = 'users_login'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    user_id = Column(Integer, ForeignKey('users_biography.id'))

    biography = relationship("DBBiography", back_populates='user_login')


class DBBiography(Base):
    __tablename__ = 'users_biography'
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    gender = Column(String)
    age = Column(Integer)

    user_login = relationship('DBLogin', back_populates='biography')

