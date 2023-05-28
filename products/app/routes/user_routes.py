from fastapi import APIRouter, Depends, Response, status, Body
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.routes.dependencies import get_db_session
from app.schemas.user import UserRequest
from app.use_cases.user import UserUseCases

router = APIRouter(prefix='/users', tags=['User'])

@router.post('/', response_model=None)
def add_user(user: UserRequest = Body(default={ 'username': 'bevila', 'password': 'bevila' }),
            db_session: Session = Depends(get_db_session)):
    uc = UserUseCases(db_session=db_session)
    uc.add_user(user=user)
    return Response(status_code=status.HTTP_201_CREATED)

@router.post('/login')
def login_user(login: OAuth2PasswordRequestForm = Depends(),
               db_session: Session = Depends(get_db_session)):
    uc = UserUseCases(db_session=db_session)

    user = UserRequest(
        username=login.username,
        password=login.password
    )
    userToken = uc.login_user(user=user)
    return userToken