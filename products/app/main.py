from fastapi import FastAPI
from app.schemas.category import Category

app = FastAPI()

@app.get('/health')
def health_check():
    return { "health_check": "healthy" }

@app.get('/category/{name}')
def get_category(name: str):
    return Category(name=name, slug=name).json()