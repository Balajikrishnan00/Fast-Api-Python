from sqlalchemy import Column, Integer, String
from database import Base


class DBModels(Base):
    __tablename__ = 'posts'
    posts_no = Column(Integer, primary_key=True, index=True)
    userid = Column(Integer)
    title = Column(String)
    body = Column(String)
