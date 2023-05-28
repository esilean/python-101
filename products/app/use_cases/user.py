from decouple import config
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.data.models import User as UserModel
from app.schemas.user import UserRequest, UserToken
from passlib.hash import pbkdf2_sha256
from datetime import datetime, timedelta
from jose import jwt, JWTError

TOKEN_SECRET = config('TOKEN_SECRET')

class UserUseCases():
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def add_user(self, user: UserRequest):
        user_on_db = self.db_session.get(UserModel, user.username)
        if user_on_db:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='username already taken')

        user_model = UserModel(
            username=user.username,
            password=pbkdf2_sha256.hash(user.password)
        )
        self.db_session.add(user_model)
        self.db_session.commit()

    def login_user(self, user: UserRequest):
        user_on_db = self.db_session.get(UserModel, user.username)
        if not user_on_db:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='invalid username or password')
    
        authenticated = pbkdf2_sha256.verify(user.password, user_on_db.password)
        if not authenticated:
            raise HTTPException(status.HTTP_400_BAD_REQUEST, detail='invalid username or password')
        
        expires_at = datetime.utcnow() + timedelta(minutes=1) 
        token_data = {
            'sub': user.username,
            'exp': expires_at
        }

        access_token = jwt.encode(claims=token_data, key=TOKEN_SECRET, algorithm='HS256')

        return UserToken(
            access_token=access_token,
            expires_at=expires_at
        )
    
    def verify_token(self, token: str):
        try:
            data = jwt.decode(token=token, key=TOKEN_SECRET, algorithms=['HS256'])
        except JWTError:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)
        
        username = data['sub']
        user_on_db = self.db_session.get(UserModel, username)
        if not user_on_db:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED)

