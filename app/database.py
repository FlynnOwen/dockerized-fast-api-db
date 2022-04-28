import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

#DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = f"postgresql://{os.getenv(POSTGRES_USER)}"\
               f":{os.getenv(POSTGRES_PASSWORD)}"\
               f"@{os.getenv(POSTGRES_SERVER)}"\
               f":{os.getenv(POSTGRES_PORT)}"\
               f"/{os.getenv(POSTGRES_DB)}"
# UPDATE ABOVE TO READ FROM Postgres
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()