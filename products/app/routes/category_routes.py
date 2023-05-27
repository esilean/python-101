from fastapi import APIRouter, Depends, Response, status, Body
from sqlalchemy.orm import Session

from app.routes.dependencies import get_db_session
from app.schemas.category import CategoryRequest, CategoryResponse
from app.use_cases.category import CategoryUseCases

router = APIRouter(prefix='/categories', tags=['Category'])

@router.post('/', response_model=None)
def add_category(category: CategoryRequest = Body(default={ 'name': 'T-Shirt', 'slug': 't-shirt' }), 
                 db_session: Session = Depends(get_db_session)) -> None:
    uc = CategoryUseCases(db_session=db_session)
    uc.add_category(category=category)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/', response_model=list[CategoryResponse])
def list_categories(db_session: Session = Depends(get_db_session)) -> list[CategoryResponse]:
    uc = CategoryUseCases(db_session=db_session)
    categories = uc.list_categories()
    return categories

@router.get('/{id}', response_model=CategoryResponse)
def list_categories(id: int, db_session: Session = Depends(get_db_session)) -> CategoryResponse:
    uc = CategoryUseCases(db_session=db_session)
    category = uc.get_category(id)
    return category

@router.delete('/{id}', response_model=None)
def delete_category(id: int,
                    db_session: Session = Depends(get_db_session)) -> None:
    uc = CategoryUseCases(db_session=db_session)
    uc.delete_category(id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)