from pydantic import BaseModel


class Human(BaseModel):
    id: int
    name: str
    gender: str
    age: int
    height: int

    class Config:
        orm_mode=True