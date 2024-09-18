"""Модуль для обробки всіх HTTP-roots для '/films' - тобто фільмів."""
from fastapi import APIRouter

from ..models.films import Film
from .. import tables

from ..database import Session    # new line

router = APIRouter(prefix="/films")


@router.get("/", response_model=list[Film])
def read_films():
    session = Session()
    films = session.query(tables.Films).all()
    session.close()
    return films
