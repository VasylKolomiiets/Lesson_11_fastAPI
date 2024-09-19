"""Модуль для обробки всіх HTTP-roots для '/films' - тобто фільмів."""
from fastapi import APIRouter
from fastapi import Depends

from ..models.films import Film, FilmCategory, FilmCreate
from ..services.films import FilmsService


router = APIRouter(prefix="/films")

# not hardcoded `film_category` param magically will be searching in query string
@router.get("/", response_model=list[Film])
def read_films(film_category: FilmCategory | None = None, service: FilmsService = Depends()):
    return service.get_all(film_category)

# Ми всього лише вказали `film_data: FilmCreate` але FastAPI буде шукати дані 
# в тілі запиту, бо запит у нас типу `post`
@router.post("/", response_model=Film)
def create_film(film_data: FilmCreate, service: FilmsService = Depends()):
    return service.create(film_data)


@router.get("/{film_id}", response_model=Film)
def read_film(film_id: int, service: FilmsService = Depends()):
    return service.get(film_id)
