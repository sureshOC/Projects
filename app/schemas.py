from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str
    role: str   # "admin" or "user"

# class UserLogin(BaseModel):
#     username: str
#     password: str
