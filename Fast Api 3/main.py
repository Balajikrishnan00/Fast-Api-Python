from fastapi import FastAPI, Depends, Response, status, HTTPException
import models
from database import engine, SessionLocal
from schemas import Blog
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/user', status_code=status.HTTP_201_CREATED)
def create(request: Blog, db: Session = Depends(get_db)):
    new_user = models.DbBlog(username=request.username, email=request.email, password=request.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/users', )
async def show_users(db: Session = Depends(get_db)):
    fetch_all_users = db.query(models.DbBlog).all()
    return fetch_all_users


@app.get('/user/{id}', status_code=200)
def show_users_id(response: Response, id: int, db: Session = Depends(get_db)):
    fetch_by_id = db.query(models.DbBlog).filter(models.DbBlog.id == id).first()
    if not fetch_by_id:
        #   response.status_code = status.HTTP_404_NOT_FOUND
        #   return {'details':f"Blog with the id {id} is not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')

    return fetch_by_id


@app.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_id(id: int, db: Session = Depends(get_db)):
    #    is_id = db.query(models.DbBlog).filter(models.DbBlog.id == id).first() #.delete(synchronize_session=False)
    #    if not is_id:
    #        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail=f'No Content')
    #    is_id.delete()
    #    db.commit()
    db.query(models.DbBlog).filter(models.DbBlog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'


@app.put('/users/{id}')
async def remove(id: int, request: Blog, db: Session = Depends(get_db)):
    db.query(models.DbBlog).filter(models.DbBlog.id == id).update({'username': request.username})
    db.commit()
    return 'updated'


"""
if __name__ == '__main__':
    apk = app
    uvicorn.run(apk, host='127.0.0.1', port=9000, debug=True)
"""
