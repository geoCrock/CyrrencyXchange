from databases import Database
from sqlalchemy import create_engine, Column, String, Integer, DECIMAL, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

from app.config import POSTGRESQL_URL

DATABASE_URL = POSTGRESQL_URL
database = Database(DATABASE_URL)
metadata = declarative_base()


class CurrencyTable(metadata):
    __tablename__ = "currency"
    id = Column(Integer, primary_key=True, index=True)
    exchanger = Column(String)
    datetime = Column(DateTime, default=func.now())
    pair = Column(String)
    price = Column(DECIMAL)


engine = create_engine(DATABASE_URL)
metadata.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
