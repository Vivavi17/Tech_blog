"""Основной модуль"""

import uvicorn
from fastapi import FastAPI

from src.articles.router import articles_router
from src.comments.router import comments_router
from src.complaints.router import complaints_router
from src.config import settings
from src.reviews.router import reviews_router
from src.users.router import router as users_router

app = FastAPI()


@app.get("/ping")
async def ping() -> str:
    """Проверка доступности сервиса"""
    return "ok"


app.include_router(users_router)
app.include_router(articles_router)
app.include_router(comments_router)
app.include_router(complaints_router)
app.include_router(reviews_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.UVICORN_HOST, port=settings.UVICORN_PORT, reload=True)
