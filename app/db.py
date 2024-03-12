import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)

DATABASE_URL = os.environ["DATABASE_URL"]


def create_database_engine():

    engine = create_engine(DATABASE_URL)
    return engine


SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=create_database_engine())


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
