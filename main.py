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