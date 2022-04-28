from pydantic import BaseModel


class HumanBase(BaseModel):
    name: str
    gender: str
    age: int
    height: int


class Human(HumanBase):
    id: int

    class Config:
        orm_mode=True


class HumanCreate(Human):
    pass