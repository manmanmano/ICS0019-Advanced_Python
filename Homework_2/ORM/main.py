from enum import unique
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey


engine = create_engine('sqlite:///diner.db', echo = True)

Base = declarative_base()


class Provider(Base):
    __tablename__ = 'PROVIDER'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ProviderName = Column(String, unique=True, nullable=False)


class Canteen(Base):
    __tablename__ = 'CANTEEN'
    ID = Column(Integer, primary_key=True, autoincrement=True)
    ProviderID = Column(Integer, ForeignKey('PROVIDER.ID'), nullable=False)
    Name = Column(String, unique=True, nullable=False)
    Location = Column(String, nullable=False)
    time_open = Column(Integer, nullable=False)
    time_closed = Column(Integer, nullable=False)
    provider = relationship("Provider", back_populates = 'CANTEEN')


Base.metadata.create_all(engine)


