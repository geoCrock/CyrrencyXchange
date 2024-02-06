from databases import Database
from sqlalchemy import create_engine, Column, String, Integer, DECIMAL, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from app.config import POSTGRESQL_URL

# Connecting to the database
DATABASE_URL = POSTGRESQL_URL
database = Database(DATABASE_URL)
metadata = declarative_base()


# Defining a model for a table in the database
class CurrencyTable(metadata):
    __tablename__ = "currency"
    id = Column(Integer, primary_key=True, index=True)
    exchanger = Column(String)
    datetime = Column(DateTime, default=func.now())
    pair = Column(String)
    price = Column(DECIMAL)


# Create a table in the database
engine = create_engine(DATABASE_URL)
metadata.metadata.create_all(bind=engine)

# Create a session to work with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
