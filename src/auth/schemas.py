from typing import Optional
from pydantic import BaseModel


class LoginItem(BaseModel):
    email: str
    password: Optional[str]
    type: str


class RegisterItem(BaseModel):
    email: str
    fullName: str
    type: str
    password: Optional[str]
    id: Optional[str]


class UserCreatedItem(BaseModel):
    id: str
    email: str


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
