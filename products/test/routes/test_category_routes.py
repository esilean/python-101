from sqlalchemy.orm import Session
from app.data.models import Category as CategoryModel
from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

client = TestClient(app)

def test_add_category_route(db_session: Session):
    body = { 
        "name": "T-Shirt",
        "slug": 't-shirt'
    }

    response = client.post('/categories', json=body)

    assert response.status_code == status.HTTP_201_CREATED

    categories_on_db = db_session.query(CategoryModel).all()
    assert len(categories_on_db) == 1
    db_session.delete(categories_on_db[0])
    db_session.commit()

def test_list_categories_route(categories_on_db):
    response = client.get('/categories')

    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert len(data) == 4
    assert data[0].get('id') == categories_on_db[0].id
    assert data[0].get('name') == categories_on_db[0].name
    assert data[0].get('slug') == categories_on_db[0].slug

def test_get_category_route():
    response = client.get('/categories/999')

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = response.json()
    assert data.get('detail') == 'category not found'

def test_delete_category_route(db_session: Session):
    category_model = CategoryModel(name='T-Shirt', slug='t-shirt')
    db_session.add(category_model)
    db_session.commit()

    response = client.delete(f'/categories/{category_model.id}')

    assert response.status_code == status.HTTP_204_NO_CONTENT

    response = client.get(f'/categories/{category_model.id}')
    assert response.status_code == status.HTTP_400_BAD_REQUEST