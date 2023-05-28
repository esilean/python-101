import re
from pydantic import validator
from app.schemas.base import CustomBaseModel
from datetime import datetime

class UserRequest(CustomBaseModel):
    username: str
    password: str

    @validator('username')
    def validate_username(cls, value):
        if not re.match('^([a-z]|[A-Z]|-|@|_)+$', value):
            raise ValueError('invalid username')
        return value

    @validator('password')
    def validate_password(cls, value):
        if len(value) < 3:
            raise ValueError('invalid password')
        return value
    
class UserResponse(CustomBaseModel):
    pass

class UserToken(CustomBaseModel):
    access_token: str
    expires_at: datetime