from fastapi import HTTPException, status
import models
from db import get_password_hash


def get_all_users(db):
    users = db.query(models.UsersDB).all()
    return users


def get_user_by_id(id, db):
    user = db.query(models.UsersDB).filter(models.UsersDB.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')
    return user.first()


def post_user(request, db):
    user = models.UsersDB(username=request.username,
                          email=request.email, password=get_password_hash(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def updated_user(id, request, db):
    user = db.query(models.UsersDB).filter(models.UsersDB.id == id)
    user.update({'password': request.password})
    db.commit()
    return f'user {id} have changed'


def deleted_user(id, db):
    user = db.query(models.UsersDB).filter(models.UsersDB.id == id).first()
    user.delete()
    db.commit()
    return f"you account has deleted"
