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
    provider = relationship("Provider", back_populates = 'canteens')


Provider.canteens = relationship("Canteen", back_populates = "provider")

Base.metadata.create_all(engine)

# add records to provider table
data = [Provider(ProviderName = "Rahva toit", canteens = [
    Canteen(
        Name = "Economics- and social science building canteen", 
        Location = "Akadeemia tee 3, SOC-building", time_open = 830, time_closed = 1830),
    Canteen(
        Name = "Library canteen", Location = "Akadeemia tee 1/Ehitajate tee 7",
        time_open = 830, time_closed = 1900),
    Canteen(
        Name = "U06 building canteen", Location = "U06 building",
        time_open = 900, time_closed = 1600)]),
    Provider(ProviderName = "Baltic Restaurants Estonia AS", canteens = [
        Canteen(
            Name = "Main building Deli cafe", Location = "Ehitajate tee 5, U01 building",
            time_open = 900, time_closed = 1630), 
        Canteen(
            Name = "Main building Daily lunch restaurant", Location = "Ehitajate tee 5, U01 building",
            time_open = 900, time_closed = 1630),
        Canteen(
            Name = "Natural Science building canteen", Location = "Akadeemia tee 15, SCI building",
            time_open = 900, time_closed = 1600),
        Canteen(
            Name = "ICT building canteen", Location = "Raja 15/Mäepealse 1", 
            time_open = 900, time_closed = 1600)]),
    Provider(ProviderName = "TTÜ Sport OÜ", canteens = [
        Canteen(
            Name = "Sports building canteen", Location = "Männiliiva 7, S01 building",
            time_open = 1100, time_closed = 2000)])]

Session = sessionmaker(bind=engine)
session = Session()

session.add_all(data)
session.commit()
#try:
#    session.add(p)
#    session.commit()
#except:
#    session.rollback()
#finally:
#    session.close()
