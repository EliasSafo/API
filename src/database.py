import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_host = os.environ["DB_HOST"]
print(db_host)
SQLALCHEMY_DATABASE_URL = (f"postgresql+psycopg2://elias:secret_123@{db_host}:5432"
                          "/learning_sql")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()