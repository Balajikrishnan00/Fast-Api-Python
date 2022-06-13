from pydantic import BaseModel


class DatabaseSchemas(BaseModel):
    userId: int
    title: str
    body: str


class ShowBlog(DatabaseSchemas):
    class Config:
        orm_mode = True
