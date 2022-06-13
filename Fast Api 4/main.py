from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, SessionLocal
from schemas import DatabaseSchemas

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', status_code=status.HTTP_200_OK)
async def index():
    return {'message': 'index page'}


@app.post('/post', status_code=status.HTTP_201_CREATED)
async def show_all_posts(request: DatabaseSchemas, db: Session = Depends(get_db)):
    post = models.DBModels(userid=request.userId, title=request.title, body=request.body)
    db.add(post)
    db.commit()
    db.refresh(post)
    return post


@app.get('/posts', status_code=status.HTTP_200_OK)
async def get_posts(db: Session = Depends(get_db)):
    all_posts = db.query(models.DBModels).all()
    return all_posts


@app.get('/posts/{userid}', status_code=status.HTTP_404_NOT_FOUND)
async def get_posts_byid(userid: int, db: Session = Depends(get_db)):
    userId = db.query(models.DBModels).filter(models.DBModels.userid == userid).all()
    if not userId:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {userid} not found')
    return userId


@app.delete('/posts/{posts_no}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(post_no: int, db: Session = Depends(get_db)):
    id = db.query(models.DBModels).filter(models.DBModels.posts_no == post_no)
    if not id:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail='204 No Content')
    id.delete()
    db.commit()
    return 'Done'


@app.put('/post/{post_id}', status_code=status.HTTP_202_ACCEPTED)
async def updated(post_id: int, request: schemas.DatabaseSchemas, db: Session = Depends(get_db)):
    details = db.query(models.DBModels).filter(models.DBModels.posts_no == post_id)
    if not details.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'{status.HTTP_404_NOT_FOUND} not Found')

    details.update({"userid": request.userId, 'title': request.title, 'body': request.body})
    db.commit()
    return 'success'


@app.get('/post_blog/{post_id}', status_code=status.HTTP_200_OK,)
async def show_blog(post_id: int, db: Session = Depends(get_db)):
    details = db.query(models.DBModels).filter(models.DBModels.posts_no == post_id).first()
    if not details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='not found')
    return details
