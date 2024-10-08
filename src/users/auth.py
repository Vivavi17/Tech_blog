"""Модуль аутентификации"""

from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from src.config import settings

pwd_context = CryptContext(schemes=["sha256_crypt"], deprecated="auto")


def get_hashed_pwd(password: str) -> str:
    """Получить хешированный пароль"""
    return pwd_context.hash(password)


def verify_pwd(password: str, hashed_password: str) -> str:
    """Верифицировать пароль"""
    return pwd_context.verify(password, hashed_password)


def create_access_token(data: dict) -> str:
    """Создаие токена доступа"""
    to_encode = data.copy()
    to_encode.update(exp=datetime.utcnow() + timedelta(minutes=settings.TOKEN_EXP_MIN))
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, settings.ALGORITHM)
    return encoded_jwt
