from app.data.connection import Session
from sqlalchemy.orm import Session as SessionType
from fastapi.security  import OAuth2PasswordBearer
from fastapi import Depends
from app.use_cases.user import UserUseCases

oauth_scheme = OAuth2PasswordBearer(tokenUrl='/users/login')

def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

def authenticate(db_session: SessionType = Depends(get_db_session),
                 token: OAuth2PasswordBearer = Depends(oauth_scheme)):
    uc = UserUseCases(db_session=db_session)
    uc.verify_token(token)
