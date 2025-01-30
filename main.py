from fastapi import FastAPI

app = FastAPI()

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

  