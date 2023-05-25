import pytest
from app.schemas.category import Category

def test_category_schema():
    category = Category(
        name='T-Shirt',
        slug='t-shirt'
    )

    assert category.dict() == {
        'name': 'T-Shirt',
        'slug': 't-shirt'
    }

def test_category_schema_invalid_slug():
    with pytest.raises(ValueError):
        category = Category(
            name='T-Shirt',
            slug='t shirt'
        )

    with pytest.raises(ValueError):
        category = Category(
            name='T-Shirt',
            slug='t@shirt'
        )