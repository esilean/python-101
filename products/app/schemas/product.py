import re
from pydantic import validator
from datetime import datetime
from app.schemas.base import CustomBaseModel
from app.schemas.category import CategoryResponse

class ProductRequest(CustomBaseModel):
    name: str
    slug: str
    price: float
    stock: int
    category_id: int

    @validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('invalid slug')
        return value
    
    @validator('price')
    def validate_price(cls, value):
        if value <= 0:
            raise ValueError('invalid price')
        return value

class ProductResponse(CustomBaseModel):
    id: int
    name: str
    slug: str
    price: float
    stock: int
    category: CategoryResponse
    created_at: datetime
