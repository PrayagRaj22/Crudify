from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional, List

route = APIRouter(prefix="/users")

# local db
users: List["UserIn"] = []


# Schema
class UserIn(BaseModel):
    username: str
    firstName: str
    lastName: str | None = None
    email: EmailStr
    age: int = 18  # Optional
    is_female: Optional[bool] = False  # Optional


class UserOut(BaseModel):
    username: str
    fullName: str | None = None
    email: EmailStr


# GET ALL USERS
@route.get("/", response_model=List[UserOut])
async def get_users():
    return [
        UserOut(
            username=user.username,
            fullName=f"{user.firstName} {user.lastName or ''}".strip(),
            email=user.email,
        )
        for user in users
    ]


# CREATE USER
@route.post("/", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserIn):
    # Basic duplicate check
    if any(u.email == user.email for u in users):
        raise HTTPException(status_code=409, detail="Email already exists")

    users.append(user)

    return UserOut(
        username=user.username,
        fullName=f"{user.firstName} {user.lastName or ''}".strip(),
        email=user.email,
    )
