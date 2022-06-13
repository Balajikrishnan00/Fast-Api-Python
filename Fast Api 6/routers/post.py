from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from repository.oauth2 import get_current_user
from repository.posts import get_all_posts, post_by_id, post_data, update_post, delete_post
from schemas import ResponsePostModel_1, PostModel, PostUpdateModel

router = APIRouter(prefix='/post',
                   tags=['Posts'])


@router.get('/', response_model=List[ResponsePostModel_1])
def get_posts(db: Session = Depends(get_db), current_users: PostModel = Depends(get_current_user)):
    return get_all_posts(db)


@router.get('/{id}', response_model=ResponsePostModel_1)
def get_post(id: int, db: Session = Depends(get_db),current_user: ResponsePostModel_1 = Depends(get_current_user)):
    return post_by_id(id, db)


@router.post('/')
def posts(request: PostModel, db: Session = Depends(get_db)):
    return post_data(request, db)


@router.put('/{id}')
def update(id: int, request: PostUpdateModel, db: Session = Depends(get_db)):
    return update_post(id, request, db)


@router.delete('/{id}')
def delete_posts(id, db: Session = Depends(get_db)):
    return delete_post(id, db)
