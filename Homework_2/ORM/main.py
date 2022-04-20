from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, UniqueConstraint, ForeignKey


engine = create_engine('sqlite:///diners.db', echo = True)

meta = MetaData()

canteen = Table(
        'CANTEEN', meta,
        Column('ID', Integer, primary_key=True),
        Column('ProviderID', Integer, ForeignKey('PROVIDER.ID'), nullable=False),
        Column('Name', String, nullable=False),
        Column('Location', String, nullable=False),
        Column('time_open', Integer, nullable=False),
        Column('time_closed', Integer, nullable=False),
        UniqueConstraint('Name'))

provider = Table(
        'PROVIDER', meta,
        Column('ID', Integer, primary_key=True),
        Column('ProviderName', String, nullable=False),
        UniqueConstraint('ProviderName'))

meta.create_all(engine)
