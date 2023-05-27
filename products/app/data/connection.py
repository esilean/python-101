from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_ON = config('TEST_ON', default=False, cast=bool)
POSTGRES_CNNSTRING = config('TEST_POSTGRES_CNNSTRING') if TEST_ON else config('POSTGRES_CNNSTRING')

engine = create_engine(POSTGRES_CNNSTRING, pool_pre_ping=True)
Session = sessionmaker(bind=engine)