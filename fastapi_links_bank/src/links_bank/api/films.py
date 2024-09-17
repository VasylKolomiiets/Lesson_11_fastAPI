"""Модуль для обробки всіх HTTP-roots для '/films' - тобто фільмів."""
from fastapi import APIRouter

router = APIRouter(prefix="/films")

@router.get("/")
def test_films_root():
    return {"films_api_test": "passed_well"}