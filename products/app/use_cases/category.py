from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.data.models import Category as CategoryModel
from app.schemas.category import CategoryRequest
from app.use_cases.mappers import category_model_to_response

class CategoryUseCases():
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def add_category(self, category: CategoryRequest):
        category_model = CategoryModel(**category.dict())
        self.db_session.add(category_model)
        self.db_session.commit()

    def list_categories(self):
        categories_on_db = self.db_session.query(CategoryModel).all()
        categories_response = [category_model_to_response(category_model) for category_model in categories_on_db]
        return categories_response
    
    def get_category(self, id: int):
        category_model = self.db_session.get(CategoryModel, id)

        if not category_model:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='category not found')
        
        return category_model_to_response(category_model=category_model)
    
    def delete_category(self, id: int):
        category_model = self.db_session.get(CategoryModel, id)

        if not category_model:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='category not found')

        self.db_session.delete(category_model)
        self.db_session.commit()