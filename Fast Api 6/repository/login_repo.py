from datetime import timedelta

from fastapi import HTTPException
from starlette import status
import models
from Token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from db import verify_password


def post_login(request, db):
    user = db.query(models.UsersDB).filter(models.UsersDB.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid username')

    if not verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid password')

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
