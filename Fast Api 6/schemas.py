from pydantic import BaseModel


class PostModel(BaseModel):
    userid: int
    title: str
    body: str


class PostUpdateModel(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


##################################################################################################################


class UsersPostModel(BaseModel):
    username: str
    email: str
    password: str


class UserPasswordUpdateModel(BaseModel):
    password: str


####################################################################################################################


class ResponseUserModel_1(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True


class ResponsePostModel_1(BaseModel):
    title: str
    body: str
    creator: ResponseUserModel_1

    class Config:
        orm_mode = True


class ResponsePostModel_2(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class ResponseUserModel_2(BaseModel):
    username: str
    email: str
    Posts: list[ResponsePostModel_2] = []

    class Config:
        orm_mode = True


############################################################################################################


class Login(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
