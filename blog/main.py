from fastapi import FastAPI , Depends
from typing import Optional
from pydantic import BaseModel
import schemas
from database import get_db
import models
from sqlalchemy.orm import Session
import hashing



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

@app.post('/user')
def create_user(request: schemas.User , db: Session = Depends(get_db)): 
    new_user = models.User(name = request.name,email = request.email,password=hashing.Hash.bcrypt(request.password) )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.delete('/user')
def delete_user(request: schemas.User, db: Session = Depends(get_db)): 
    excluded_user = db.query(models.User).filter(models.User.id == request.id).first()
    
    if not excluded_user:  # Verifica se o usuário existe antes de deletar
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    db.delete(excluded_user)
    db.commit()
    
    return {"message": "Usuário deletado com sucesso!"}  # ✅ Retorna confirmação

