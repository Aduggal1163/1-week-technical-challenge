import models
from pydantic import BaseModel
from typing import Annotated
from fastapi import FastAPI,HTTPException,status,Depends
from database import engine,sessionLocal
from sqlalchemy.orm import Session
app=FastAPI()
models.Base.metadata.create_all(bind=engine)

class NotesBase(BaseModel):
    id: int
    title:str
    content:str

def get_db():
    db=sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency= Annotated[Session,Depends(get_db)]

@app.post('/notes',status_code=status.HTTP_201_CREATED)
async def create_notes(note : NotesBase, db:db_dependency):
    db_note = models.Notes(
        title = note.title,
        content=note.content
    )
    if db_note.title is None or db_note.content is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Fill details properly'
        )
    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    return db_note

@app.get('/all',status_code=status.HTTP_200_OK)
async def get_all(db:db_dependency):
    return db.query(models.Notes).all()