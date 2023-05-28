from fastapi import APIRouter, Depends, Response, status, Body
from sqlalchemy.orm import Session

from app.routes.dependencies import get_db_session, authenticate
from app.schemas.category import CategoryRequest, CategoryResponse
from app.use_cases.category import CategoryUseCases

router = APIRouter(prefix='/categories', tags=['Category'], dependencies=[Depends(authenticate)])

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=None)
def add_category(category: CategoryRequest = Body(default={ 'name': 'Animes', 'slug': 'animes' }), 
                 db_session: Session = Depends(get_db_session)) -> None:
    uc = CategoryUseCases(db_session=db_session)
    uc.add_category(category=category)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/', status_code=status.HTTP_200_OK, response_model=list[CategoryResponse])
def list_categories(db_session: Session = Depends(get_db_session)) -> list[CategoryResponse]:
    uc = CategoryUseCases(db_session=db_session)
    categories = uc.list_categories()
    return categories

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=CategoryResponse)
def get_category(id: int, db_session: Session = Depends(get_db_session)) -> CategoryResponse:
    uc = CategoryUseCases(db_session=db_session)
    category = uc.get_category(id)
    return category

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, response_model=None)
def delete_category(id: int,
                    db_session: Session = Depends(get_db_session)) -> None:
    uc = CategoryUseCases(db_session=db_session)
    uc.delete_category(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)