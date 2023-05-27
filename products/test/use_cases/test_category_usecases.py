from sqlalchemy.orm import Session
from app.use_cases.category import CategoryUseCases
from app.data.models import Category as CategoryModel
from app.schemas.category import CategoryRequest, CategoryResponse
import pytest
from fastapi import HTTPException

def test_add_category_uc(db_session: Session):
    uc = CategoryUseCases(db_session)

    category = CategoryRequest(
        name='T-Shirt',
        slug='t-shirt'
    )

    uc.add_category(category=category)

    categories_on_db = db_session.query(CategoryModel).all()

    assert len(categories_on_db) == 1
    assert categories_on_db[0].name == 'T-Shirt'
    assert categories_on_db[0].slug == 't-shirt'

    db_session.delete(categories_on_db[0])
    db_session.commit()

def test_list_categories(categories_on_db, db_session: Session):
    uc = CategoryUseCases(db_session=db_session)

    categories = uc.list_categories()

    assert type(categories[0]) == CategoryResponse
    assert categories[0].id == categories_on_db[0].id
    assert categories[0].name == categories_on_db[0].name
    assert categories[0].slug == categories_on_db[0].slug

def test_get_category(db_session: Session):
    uc = CategoryUseCases(db_session=db_session)

    with pytest.raises(HTTPException):
        uc.get_category(999)


def test_delete_category(db_session: Session):
    category = CategoryModel(name='T-Shirt', slug='t-shirt')
    db_session.add(category)
    db_session.commit()

    uc = CategoryUseCases(db_session=db_session)
    uc.delete_category(id=category.id)

    category = db_session.get(CategoryModel, category.id)
    assert category == None
