"""Registro, login y 'quién soy'."""
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select

from dependencies import CurrentUser, SessionDep, credentials_error
from models import Token, User, UserCreate, UserMe
from security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserMe, status_code=201)
def register(data: UserCreate, db: SessionDep):
    # me fijo que no exista otro con el mismo username
    statement = select(User).where(User.username == data.username)
    usuario_existente = db.exec(statement).first()
    if usuario_existente:
        raise HTTPException(status_code=409, detail="El usuario ya existe")

    nuevo_usuario = User(
        username=data.username,
        hashed_password=hash_password(data.password)
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


@router.post("/login", response_model=Token)
def login(form: Annotated[OAuth2PasswordRequestForm, Depends()], db: SessionDep):
    # TODO 3: iniciar sesión (el formulario trae form.username y form.password)
    #   a) busca el User por username
    #   b) si no existe, o verify_password(form.password, user.hashed_password) es False
    #      → raise credentials_error()      (mismo error para ambos casos: ¿por qué?)
    #   c) return Token(access_token=create_access_token(user.id))
    raise HTTPException(status.HTTP_501_NOT_IMPLEMENTED, "TODO 3: login")


@router.get("/me", response_model=UserMe)
def me(current_user: CurrentUser):  # ya resuelto: funciona cuando hagas el TODO 4
    return current_user
