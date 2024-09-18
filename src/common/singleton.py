"""Модуль класса Singleton"""


class Singleton:
    """Класс с единственным экземпляром"""

    singleton = None
    dao = None

    def __new__(cls, *args, **kwargs):
        """Создать первый объект и/или вернуть его"""
        if not cls.singleton:
            cls.singleton = super().__new__(cls, *args, **kwargs)
        return cls.singleton
