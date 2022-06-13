from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# sqlite:////absolute/path/to/file.db
# D:\Fast Api\Fast Api 3\users.db

SQLALCHEMY_DATABASE = 'sqlite:///users.db'

engine = create_engine(SQLALCHEMY_DATABASE, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
