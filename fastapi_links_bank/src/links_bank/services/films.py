"""Модуль для збереження 'бізнес-логікі' сутності проекту `films`.

    Тобто клас, який опрацьовує наші фільми.
"""
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables
from ..database import get_session


class FilmsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_all(self) -> list[tables.Films]:
        films = self.session.query(tables.Films).all()
        return films
