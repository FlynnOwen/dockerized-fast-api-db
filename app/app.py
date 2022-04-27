from fastapi import FastAPI
from pydantic import BaseModel

import models
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


@app.get('/human/{human_id}', tags=["human"] )
async def get_human(human_id) -> dict:
    return {"message": "This is your human"}


@app.post('/human/{human_id}', tags=["human"] )
async def make_human(human_id) -> dict:
    return {"message": "This is your human"}