import pytest
from sqlalchemy.orm import Session as SessionType
from app.data.connection import Session
from app.data.models import Category as CategoryModel

@pytest.fixture()
def db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()

@pytest.fixture()
def categories_on_db(db_session: SessionType):
    categories = [
        CategoryModel(name='T-Shirt', slug='t-shirt'),
        CategoryModel(name='Dress', slug='dress'),
        CategoryModel(name='Skirt', slug='skirt'),
        CategoryModel(name='Jeans', slug='jeans')
    ]

    for category in categories:
        db_session.add(category)
    db_session.commit()

    for category in categories:
        db_session.refresh(category)

    yield categories

    for category in categories:
        db_session.delete(category)
    db_session.commit()