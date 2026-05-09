from typing import List
from fastapi import FastAPI, HTTPException, Depends
from db import  SessionDep, create_all_tables
from sqlmodel import select, Session, SQLModel, create_engine
from model import Dog
from db import engine, get_session

app = FastAPI()

@app.on_event("startup")
def startup():
    SQLModel.metadata.create_all(engine)

@app.post("/DOGS", response_model=Dog)
async def create_dog(dog: Dog, session: Session = Depends(get_session)):
    session.add(dog)
    session.commit()
    session.refresh(dog)
    return dog

@app.get("/DOGS", response_model=List[Dog])
async def get_all_dogs(session: Session = Depends(get_session)):
    dogs = session.exec(select(Dog)).all()
    return dogs


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
