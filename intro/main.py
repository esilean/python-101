from dotenv import load_dotenv
from fastapi import FastAPI
from app.routers import router

load_dotenv()
app = FastAPI()

app.include_router(router)

@app.get('/')
def hello():
    return { "hello": "world" }