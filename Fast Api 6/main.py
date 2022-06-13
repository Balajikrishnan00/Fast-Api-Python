from fastapi import FastAPI
import models
from database import engine
from routers import post, users, auth

app = FastAPI()
models.Base.metadata.create_all(engine)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
'''
@app.get('/posts', response_model=List[ResponsePostModel_1], status_code=status.HTTP_200_OK, tags=['Posts'])
def get_posts(db: Session = Depends(get_db)):
    post = db.query(models.PostsDB)
    if not post.all():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f 'no data found')
    return post.all()


@app.get('/posts/{id}', response_model=ResponsePostModel_1, tags=['Posts'])
def get_post(id: int, db: Session = Depends(get_db)):
    Posts = db.query(models.PostsDB).filter(models.PostsDB.id == id)
    if not Posts.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There is No Data Found')
    return Posts.first()


@app.post('/posts', tags=['Posts'])
def posts(request: PostModel, db: Session = Depends(get_db)):
    new_posts = models.PostsDB(userId=request.userid, title=request.title, body=request.body)
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return new_posts


@app.put('/post/{id}', tags=['Posts'])
def update(id: int, request: PostUpdateModel, db: Session = Depends(get_db)):
    current_post = db.query(models.PostsDB).filter(models.PostsDB.id == id)
    current_post.update({'title': request.title, 'body': request.body})
    db.commit()
    return f'posts {id}  updated'


@app.delete('/post/{id}', tags=['Posts'])
def delete_posts(id, db: Session = Depends(get_db)):
    post = db.query(models.PostsDB).filter(models.PostsDB.id == id)
    post.delete()
    db.commit()
    return f'post {id} deleted'


#####################################################################################################
#                                                                                                   #
#                                       UsersModel                                                  #
#                                                                                                   #
#####################################################################################################


@app.get('/users', response_model=List[ResponseUserModel_1], tags=['Users'])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.UsersDB).all()
    return users


@app.get('/user/{id}', response_model=ResponseUserModel_2, tags=['Users'])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.UsersDB).filter(models.UsersDB.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'id {id} not found')
    return user.first()


@app.post('/user', tags=['Users'])
def post_user(request: UsersPostModel, db: Session = Depends(get_db)):
    user = models.UsersDB(username=request.username,
                          email=request.email, password=get_password_hash(request.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.put('/user/{id}', tags=['Users'])
def update_user(id: int, request: UserPasswordUpdateModel, db: Session = Depends(get_db)):
    user = db.query(models.UsersDB).filter(models.UsersDB.id == id)
    user.update({'password': request.password})
    db.commit()
    return f 'user {id} have changed'


@app.delete('/user/{id}', tags=['Users'])
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.UsersDB).filter(models.UsersDB.id == id).first()
    user.delete()
    db.commit()
    return f"you account has deleted"

'''
