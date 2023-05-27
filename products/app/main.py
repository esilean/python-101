from fastapi import FastAPI
from app.routes.category_routes import router as category_routes


app = FastAPI()

@app.get('/health', tags=['HealthCheck'])
def health_check():
    return { "health_check": "healthy" }

app.include_router(category_routes)