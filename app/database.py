
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine

from dotenv import load_dotenv
import os


load_dotenv()

DB_NAME=os.getenv("DB_NAME")
DB_HOST=os.getenv("DB_HOST")
DB_PORT=os.getenv("DB_PORT")
DB_USER=os.getenv("DB_USER")
DB_PASSWORD=os.getenv("DB_PASSWORD")



DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass