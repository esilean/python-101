import re
from pydantic import validator
from app.schemas.base import CustomBaseModel

class CategoryRequest(CustomBaseModel):
    name: str
    slug: str

    @validator('slug')
    def validate_slug(cls, value):
        if not re.match('^([a-z]|-|_)+$', value):
            raise ValueError('invalid slug')
        return value
    
class CategoryResponse(CategoryRequest):
    id: int
    