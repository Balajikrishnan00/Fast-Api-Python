from fastapi import HTTPException
from starlette import status
import models


def get_all_posts(db):
    post = db.query(models.PostsDB)
    if not post.all():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no data found')
    return post.all()


def post_by_id(id, db):
    Posts = db.query(models.PostsDB).filter(models.PostsDB.id == id)
    if not Posts.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'There is No Data Found')
    return Posts.first()


def post_data(request, db):
    new_posts = models.PostsDB(userId=request.userid, title=request.title, body=request.body)
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return new_posts


def update_post(id, request, db):
    current_post = db.query(models.PostsDB).filter(models.PostsDB.id == id)
    current_post.update({'title': request.title, 'body': request.body})
    db.commit()
    return f'posts {id}  updated'


def delete_post(id, db):
    post = db.query(models.PostsDB).filter(models.PostsDB.id == id)
    post.delete()
    db.commit()
    return f'post {id} deleted'
