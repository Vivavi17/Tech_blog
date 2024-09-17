"""Основной модуль"""

import uvicorn
from fastapi import FastAPI
from src.articles.router import articles_router
from src.reviews.router import reviews_router
from src.complaints.router import complaints_router
from src.comments.router import comments_router
from src.users.router import router as users_router

app = FastAPI()


@app.get("/ping")
async def ping() -> str:
    """Проверка доступности сервера"""
    return "ok"


app.include_router(users_router)
app.include_router(articles_router)
app.include_router(comments_router)
app.include_router(complaints_router)
app.include_router(reviews_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
