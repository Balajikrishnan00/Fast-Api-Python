from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from repository.user import get_all_users, get_user_by_id, updated_user, deleted_user, post_user
from schemas import ResponseUserModel_1, ResponseUserModel_2, UsersPostModel, UserPasswordUpdateModel

router = APIRouter(
    prefix='/user',
    tags=['Users'])


@router.get('/', response_model=List[ResponseUserModel_1])
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get('/{id}', response_model=ResponseUserModel_2)
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_by_id(id,db)


@router.post('/')
def post_user_data(request: UsersPostModel, db: Session = Depends(get_db)):
    return post_user(request, db)


@router.put('/{id}')
def update_user(id: int, request: UserPasswordUpdateModel, db: Session = Depends(get_db)):
    return updated_user(id, request, db)


@router.delete('/{id}')
def delete_user(id: int, db: Session = Depends(get_db)):
    return deleted_user(id, db)
