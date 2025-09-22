from fastapi import APIRouter, Depends, status, HTTPException, Form
# from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_db
from src.auth.pass_utils import verify_password
from src.auth.repo import UserRepository
from src.auth.schema import Token, UserCreate, UserResponce
from src.auth.utils import create_access_token, create_refresh_token, decode_token


router = APIRouter()

from fastapi import Form, Depends
from pydantic import BaseModel

class OAuth2EmailRequestForm:
    def __init__(
        self,
        email: str = Form(...),
        password: str = Form(...),
        scope: str = Form(""),
        grant_type: str | None = Form(None, regex="password"),
        client_id: str | None = Form(None),
        client_secret: str | None = Form(None),
    ):
        self.email = email
        self.password = password
        self.scopes = scope.split()
        self.grant_type = grant_type
        self.client_id = client_id
        self.client_secret = client_secret



@router.post ("/register", response_model=UserResponce, status_code=status.HTTP_201_CREATED)
async def register(
        user_create: UserCreate,
        db: AsyncSession = Depends(get_db),
):
    user_repo = UserRepository(db)
    user = await user_repo.get_user_by_email(user_create.email)
    if user:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT,detail = "Username already registered")
    user = await user_repo.create_user(user_create)
    return user

@router.post("/token", response_model=Token)
async def login_for_access_token(
    email: EmailStr = Form(...),
    password: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    user_repo = UserRepository(db)
    user = await user_repo.get_user_by_email(email)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect email or password",
            headers = {"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub":user.username})
    refresh_token = create_refresh_token(data={"sub":user.username})
    return Token(access_token = access_token, refresh_token = refresh_token, token_type = "bearer")

@router.post("/refresh", response_model=Token, status_code=status.HTTP_201_CREATED)
async def refresh_tokens(
    refresh_token: str, db: AsyncSession = Depends(get_db)
):
    token_data = decode_token(refresh_token)
    user_repo = UserRepository(db)
    user = await user_repo.get_user_by_username(token_data.username)
    if not user:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Incorrect username or password",
            headers = {"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub":user.username})
    refresh_token = create_refresh_token(data={"sub":user.username})
    return Token(access_token = access_token, refresh_token = refresh_token, token_type = "bearer")
