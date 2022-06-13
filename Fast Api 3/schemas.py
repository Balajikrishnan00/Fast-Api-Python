from pydantic import BaseModel


class Blog(BaseModel):
    username: str
    email: str
    password: str
