"""Модуль для обробки всіх HTTP-roots для '/films' - тобто фільмів."""
from fastapi import APIRouter

from ..models.films import Film

router = APIRouter(prefix="/films")


@router.get("/", response_model=list[Film])
def read_films():
    return films