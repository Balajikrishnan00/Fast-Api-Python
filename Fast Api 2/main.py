from typing import Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# get  operation
@app.get('/')  # base path
def index():
    return {'data': "index"}


@app.get('/posts')
def show_posts(skip: int = 0, limit: int = 10, sort: Optional[str] = None, ):
    #   return f'{skip} {limit}'
    post: list = ['hai', 'welcome', 'balaji']

    return post


@app.get('/posts/unpublished')
def unpublished():
    return {'data': 'unpublished'}


@app.get('/posts/{id}')
def show_filter_id(id: int):
    return {'post id': id}


@app.get('/about')
def about_page():
    return {'data': 'about page'}


@app.get('/posts/{id}/comments')
def comment_from_id(id: int):
    return {'data': f'{id} comment'}

""""
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = None


@app.post('/posts')
def post_details(req: Blog):
    return f'blog is created {req.title} {req.body} {req.published}'
"""


if __name__ == '__main__':
    api_apk = app
    uvicorn.run(api_apk, host='127.0.0.1',port=100)