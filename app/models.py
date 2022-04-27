from sqlalchemy import Boolean, Column, Integer, String
from database import Base


class Human(Base):
    __tablename__ = 'humans'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    age = Column(Integer)
    height = Column(Integer)
