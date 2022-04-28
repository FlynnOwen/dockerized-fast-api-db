from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/', tags=["root"] )
async def read_root() -> dict:
    return {"message": "Welcome to the FastAPI Dockerized app!"}


@app.get('/human/', tags=["human"], response_model=schemas.Human)
async def get_human(human_id: int, db: Session = Depends(get_db)):
    your_human = db.query(models.Human).filter(models.Human.id == human_id).one()

    return your_human


@app.post('/human/', tags=["human"], response_model=schemas.Human)
async def make_human(human: schemas.Human, db: Session = Depends(get_db)):
    db_human = models.Human(**human.dict())
    db.add(db_human)
    db.commit()
    db.refresh(db_human)

    return db_human