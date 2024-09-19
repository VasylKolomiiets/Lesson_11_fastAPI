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

    def _get(self, film_id: int) -> tables.Films:
        film = self.session.query(tables.Films).filter_by(id_4=film_id).first()

        if not film:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Фільм з ключем {film_id} не знайдено.",
            )
        return film

    def get_all(self, film_category: FilmCategory | None = None) -> list[tables.Films]:
        
        query = self.session.query(tables.Films)
        if film_category:
            query = query.filter_by(category=film_category)
        return query.all()
    
    def get(self, film_id: int) -> tables.Films:
        return self._get(film_id)

    def create(self, film_data: FilmCreate) -> tables.Films:
        film = tables.Films(**film_data.model_dump())
        self.session.add(film)
        self.session.commit()
        return film
    
    def update(self, film_id: int, film_data: FilmCreate) -> tables.Films:
        film = self._get(film_id)
        for field, value in film_data:   # динамічне оновлення полів об'єкту `film`
            setattr(film, field, value)
        self.session.commit()
        return film
    
    def delete(self, film_id: int) -> tables.Films:   
        film = self._get(film_id)
        self.session.delete(film)
        self.session.commit()
        