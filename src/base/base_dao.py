"""Модуль с родительским классом ДАО"""

from sqlalchemy import delete, insert, select, update

from src.database import async_session_maker


class BaseDAO:
    """Базовый интерфейс CRUD в таблицу"""

    model = None

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        """Поиск единственной записи"""
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    @classmethod
    async def find_all(cls, limit=None, offset=None, order_by=None, **filter_by):
        """Получение статей с фильтрацией и пагинацией"""
        async with async_session_maker() as session:
            query = (
                select(cls.model.__table__)
                .filter_by(**filter_by)
                .order_by(order_by)
                .offset(offset)
                .limit(limit)
            )
            result = await session.execute(query)
        return result.mappings().all()

    @classmethod
    async def add(cls, **data):
        """Добавление записи в таблицу"""
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data).returning(cls.model)
            result = await session.execute(query)
            await session.commit()
            return result.scalar()

    @classmethod
    async def update(cls, object_id, **data):
        """Обновление данных записи по ID"""
        async with async_session_maker() as session:
            query = (
                update(cls.model)
                .where(cls.model.id == object_id)
                .values(**data)
                .returning(cls.model)
            )
            result = await session.execute(query)
            await session.commit()
            return result.scalar()

    @classmethod
    async def delete(cls, **filter_by):
        """Удаление записи"""
        async with async_session_maker() as session:
            query = delete(cls.model).filter_by(**filter_by)
            await session.execute(query)
            await session.commit()
