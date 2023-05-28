from fastapi import APIRouter, Depends, Response, status, Body
from sqlalchemy.orm import Session

from app.routes.dependencies import get_db_session, authenticate
from app.schemas.product import ProductRequest, ProductResponse
from app.use_cases.product import ProductUseCases

router = APIRouter(prefix='/products', tags=['Product'], dependencies=[Depends(authenticate)])

@router.post('/', response_model=None)
def add_product(product: ProductRequest = Body(default={ 'name': 'Demon Slayer', 'slug': 'demon-slayer', 'price': 100.99, 'stock': 1, 'category_id': 0 }),
                db_session: Session = Depends(get_db_session)):
    uc = ProductUseCases(db_session=db_session)
    uc.add_product(product)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/', response_model=list[ProductResponse])
def list_products(db_session: Session = Depends(get_db_session)):
    uc = ProductUseCases(db_session=db_session)
    products = uc.list_products()
    return products