from app.data.models import Category as CategoryModel
from app.schemas.category import CategoryResponse

def category_model_to_response(category_model: CategoryModel):
    return CategoryResponse(**category_model.__dict__)