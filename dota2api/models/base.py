from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def initializeBase(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)