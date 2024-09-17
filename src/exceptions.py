from fastapi import HTTPException, status


class BlogExceptions(HTTPException):
    """Базовый класс ошибок"""

    status_code = 500
    detail = ""

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(BlogExceptions):
    """Ошибка создания пользователя"""

    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"


class UserDoesntExistsException(BlogExceptions):
    """Ошибка доступа пользователя"""

    status_code = status.HTTP_401_UNAUTHORIZED


class UserRightsException(BlogExceptions):
    """Ошибка доступа пользователя"""

    status_code = status.HTTP_403_FORBIDDEN


class IncorrectLoginOrPasswordException(BlogExceptions):
    """Ошибка входа пользователя"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный логин или пароль"


class TokenAbsentException(BlogExceptions):
    """Ошибка токена"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"


class IncorrectTokenFormatException(BlogExceptions):
    """Ошибка токена"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"

class ArticleNotFoundException(BlogExceptions):
    """Ошибка доступа статьи"""

    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Статья не найдена"
