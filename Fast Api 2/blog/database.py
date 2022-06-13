from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlite3 import *

from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine('sqlite:///./blog.db', connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
