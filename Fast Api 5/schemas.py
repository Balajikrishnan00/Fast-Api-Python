from pydantic import BaseModel

# User


class UserNameUpdate(BaseModel):
    username: str

    class Config:
        orm_mode = True

# UserDetails


class UsersDetails(BaseModel):
    firstname: str
    lastname: str
    gender: str
    age: int


class UserDetails(BaseModel):
    firstname: str
    lastname: str
    gender: str
    age: int

    class Config:
        orm_mode = True


class ResModel(BaseModel):
    username: str
    email: str
    biography: UserDetails

    class Config:
        orm_mode = True


class UserLoginBlog(BaseModel):
    username: str
    email: str
    password: str
    user_id: int


