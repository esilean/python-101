from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_CNNSTRING = config('POSTGRES_CNNSTRING')

engine = create_engine(POSTGRES_CNNSTRING, pool_pre_ping=True)
Session = sessionmaker(bind=engine)