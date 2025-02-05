from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]
    pass

@app.get('/')
def index():
    return {'data': 
            {"name" : "dudz"
             }
             }

@app.get('/about')
def index():
    return {'data': 
            {"second" : "dudz"
            }
            }

@app.get('/blog')
def index(limit = 12, published: bool =True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} blogs from the db"}
    return {"data": f"infelizmente é {published}"}

@app.post("blog")
def create_blog(request: Blog):
    return {"data": f"just posted{request.title}"}

@app.get("/blog/unpublished")
def unpublished():
    return{ 'data' : 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id:int):
    #fetch blog with id = id
    return {"data" : id}

@app.get("/blog/{id}/comments")
def comments(id):
    #fetch comments from blog with id
    return {"data" : {"1","2 "}}

  