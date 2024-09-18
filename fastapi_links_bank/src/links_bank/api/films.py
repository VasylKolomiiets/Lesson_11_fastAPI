"""Модуль для обробки всіх HTTP-roots для '/films' - тобто фільмів."""
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from ..models.films import Film
from .. import tables

from ..database import get_session

router = APIRouter(prefix="/films")


@router.get("/", response_model=list[Film])
def read_films(session: Session = Depends(get_session) ):
    films = session.query(tables.Films).all()
    return films
