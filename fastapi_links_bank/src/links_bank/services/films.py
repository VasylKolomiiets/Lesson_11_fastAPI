"""Модуль для збереження 'бізнес-логікі' сутності проекту `films`.

    Тобто клас, який опрацьовує наші фільми.
"""
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session
from ..models.films import FilmCategory, FilmCreate


class FilmsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self, film_category: FilmCategory | None = None) -> list[tables.Films]:
        
        query = self.session.query(tables.Films)
        if film_category:
            query = query.filter_by(category=film_category)
        return query.all()

    def create(self, film_data: FilmCreate) -> tables.Films:
        film = tables.Films(**film_data.model_dump())
        self.session.add(film)
        self.session.commit()
        return film