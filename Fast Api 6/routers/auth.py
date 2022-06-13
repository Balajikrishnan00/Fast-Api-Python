from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from db import get_db
from repository.login_repo import post_login
from schemas import Login

router = APIRouter(
    prefix='/authentication',
    tags=['login']
)


@router.post('/')
def login_post(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return post_login(request, db)
