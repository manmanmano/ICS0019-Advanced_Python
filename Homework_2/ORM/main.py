from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String 
from sqlalchemy import UniqueConstraint, ForeignKey


engine = create_engine('sqlite:///diners.db', echo = True)
conn = engine.connect()


def createTables():
    meta = MetaData()

    global canteen
    canteen = Table(
            'CANTEEN', meta,
            Column('ID', Integer, primary_key=True, autoincrement=True),
            Column('ProviderID', Integer, ForeignKey('PROVIDER.ID'), nullable=False),
            Column('Name', String, nullable=False),
            Column('Location', String, nullable=False),
            Column('time_open', Integer, nullable=False),
            Column('time_closed', Integer, nullable=False),
            UniqueConstraint('Name'))

    global provider
    provider = Table(
            'PROVIDER', meta,
            Column('ID', Integer, primary_key=True, autoincrement=True),
            Column('ProviderName', String, nullable=False),
            UniqueConstraint('ProviderName'))

    meta.create_all(engine)

    print("Tables created successfully!")


def createRecords(): 
    conn.execute(provider.insert(), [
        {'ProviderName':'Rahva toit'},
        {'ProviderName':'Baltic Restaurants Estonia AS'},
        {'ProviderName':'TTÜ Sport OÜ'},
        {'ProviderName':'bitStop Kohvik OÜ'},])



if __name__ == "__main__":
    print("\n")
    createTables()
    createRecords()
    conn.close()
