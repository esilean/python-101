from app.data.models import Category as CategoryModel
from app.data.models import Product as ProductModel
from app.schemas.category import CategoryResponse
from app.schemas.product import ProductResponse

def category_model_to_response(category_model: CategoryModel) -> CategoryResponse:
    return CategoryResponse(**category_model.__dict__)

def product_model_to_response(product_model: ProductModel) -> ProductResponse:
    return ProductResponse(
            id=product_model.id,
            name=product_model.name,
            slug=product_model.slug,
            price=product_model.price,
            stock=product_model.stock,
            category=CategoryResponse(
                id=product_model.category.id,
                name=product_model.category.name,
                slug=product_model.category.slug
            ),
            created_at=product_model.created_at
            )