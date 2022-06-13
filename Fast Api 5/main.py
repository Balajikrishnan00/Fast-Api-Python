from typing import List

from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
from database import engine
from db_connection import get_db
from possword import get_password_hash
from schemas import ResModel, UserNameUpdate, UsersDetails, UserDetails, UserLoginBlog
from passlib.context import CryptContext

users_Api = FastAPI()

models.Base.metadata.create_all(engine)

# response_model=List[ResModel]


@users_Api.get('/users', response_model=List[ResModel], tags=['Users Login Details'])
def get_data_from_server(db: Session = Depends(get_db)):
    all_users = db.query(models.DBLogin)
    if not all_users.all():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Data Not Found')
    return all_users.all()


@users_Api.get('/user/{id}', response_model=ResModel, tags=['Users Login Details'])
def get_data_from_server_by_id(id, db: Session = Depends(get_db)):
    user_id = db.query(models.DBLogin).filter(models.DBLogin.id == id)
    if not user_id.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')
    return user_id.first()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@users_Api.post('/users', tags=['Users Login Details'])
def post_data_to_server(request: UserLoginBlog, db: Session = Depends(get_db)):
    # send = models.DBModel(username=request.username, email=request.email, password=request.password)
    # hashed_password = pwd_context.hash(request.password)
    # pas = pwd_context.encrypt(hashed_password)

    send = models.DBLogin(username=request.username, email=request.email,
                          password=get_password_hash(request.password), user_id=request.user_id)
    db.add(send)
    db.commit()
    db.refresh(send)
    return f'user {send.username} added'


@users_Api.put('/user/{id}', tags=['Users Login Details'])
def update_data_from_server(id: int, request: UserNameUpdate, db: Session = Depends(get_db)):
    user = db.query(models.DBLogin).filter(models.DBLogin.id == id)
    user.update({'username': request.username})
    return 'updated'


@users_Api.delete('/user_del/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Users Login Details'])
def destroy_data_from_server(id: int, db: Session = Depends(get_db)):
    del_id = db.query(models.DBLogin).filter(models.DBLogin.id == id)
    if not del_id.first():
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'user id {id} not found')
    del_id.delete()
    db.commit()
    return 'deleted'


#######################################################################################################
#                                                                                                     #
#                                       USER_BIOGRAPHY                                                #
#                                                                                                     #
#######################################################################################################


@users_Api.get('/user_details', tags=['Users Biography'], response_model=List[UsersDetails])
def all_user_details(db: Session = Depends(get_db)):
    users_details = db.query(models.DBBiography).all()
    if not users_details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Data Not Found')
    return users_details


@users_Api.post('/users_details', tags=['Users Biography'])
def send_user_details(request: UsersDetails, db: Session = Depends(get_db)):
    details = models.DBBiography(firstname=request.firstname,
                                 lastname=request.lastname,
                                 gender=request.gender,
                                 age=request.age)
    db.add(details)
    db.commit()
    db.refresh(details)
    return 'user added'


@users_Api.get('/user_details/{id}', status_code=status.HTTP_200_OK, tags=['Users Biography'],
               response_model=UserDetails)
def get_user_detail_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.DBBiography).filter(models.DBBiography.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')
    return user.first()


@users_Api.put('/update_users/{id}', tags=['Users Biography'])
def put_method(id, request: UsersDetails, db: Session = Depends(get_db)):
    user = db.query(models.DBBiography).filter(models.DBBiography.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')
    user.update({"firstname": request.firstname, 'lastname': request.lastname,
                 'gender': request.gender, "age": request.age})
    db.commit()
    return 'user updated'


@users_Api.delete('/user/{id]', tags=['Users Biography'])
def delete_method(id, db: Session = Depends(get_db)):
    user = db.query(models.DBBiography).filter(models.DBBiography.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'id {id} No Content')
    user.delete()
    db.commit()
    return 'user deleted'
