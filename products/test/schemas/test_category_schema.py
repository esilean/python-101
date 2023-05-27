import pytest
from app.schemas.category import CategoryRequest

def test_category_schema():
    category = CategoryRequest(
        name='T-Shirt',
        slug='t-shirt'
    )

    assert category.dict() == {
        'name': 'T-Shirt',
        'slug': 't-shirt'
    }

def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        category = CategoryRequest(
            name='T-Shirt',
            slug='t shirt'
        )

    with pytest.raises(ValueError):
        category = CategoryRequest(
            name='T-Shirt',
            slug='t@shirt'
        )