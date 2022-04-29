import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

#DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = f"postgresql://FlynnTest:FlynnTest123@db:5432/db"
# UPDATE ABOVE TO READ FROM Postgres
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
