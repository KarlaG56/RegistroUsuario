from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DATABASE_URI = 'sqlite:///nombre_base_de_datps'

engine = create_engine(DATABASE_URI)
Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(bind=engine)
