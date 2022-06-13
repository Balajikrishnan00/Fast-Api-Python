from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# @app.get('/blog?limet=10&published=true')

@app.get('/blog')
def index(limit: int = 10, published: bool = 10, sort: Optional[str] = None):
    if published:
        return {'data': f"{limit} published  blog list from database"}
    else:
        return {'data': f'{limit} blog list from db'}


@app.get('/about')
def about():
    return {'data': 'this is about page'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blog'}


@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}


@app.get('/blog/{id}/comments')
def comments(id, limit=10):
    # fetch comment of blog with id = id
    return limit
    # return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None


@app.post('/blog')
def create_blog(request: Blog):
    return {'data': f" title :{request.title}, body :{request.body},published : {request.published}"}
    # return {'data': "blog created"}
