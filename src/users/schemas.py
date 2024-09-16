from pydantic import BaseModel, EmailStr, Field


class UsersLoginS(BaseModel):
    email: EmailStr
    hashed_password: str


class UsersAuthS(UsersLoginS, BaseModel):
    username: str = Field(max_length=20)
