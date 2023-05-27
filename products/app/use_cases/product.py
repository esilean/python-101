from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.data.models import Product as ProductModel
from app.data.models import Category as CategoryModel
from app.schemas.product import ProductRequest
from app.use_cases.mappers import product_model_to_response

class ProductUseCases:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def add_product(self, product: ProductRequest):
        category = self.db_session.get(CategoryModel, product.category_id)
        if not category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='category not found')

        product_model = ProductModel(**product.dict())

        self.db_session.add(product_model)
        self.db_session.commit()

    def list_products(self):
        products_on_db = self.db_session.query(ProductModel).all()
        products = [product_model_to_response(product) for product in products_on_db]
        return products