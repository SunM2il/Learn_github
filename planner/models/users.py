from sqlmodel import SQLModel, Field
from pydantic import  BaseModel, EmailStr


class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    email: EmailStr
    password: str

    class Config:
        schema_extra = {
            "example": {
                "email": "fastapi@devhub.in.th",
                "password": "strong!!",
            }
        }


class UserSignIn(SQLModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra  = {
            "example": {
                "email": "fastapi@devhub.in.th",
                "password": "strong!!",
            }
        }


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
