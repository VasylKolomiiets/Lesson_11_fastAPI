"""Класи-моделі, що використовуються для сутності `фільми`."""
from enum import Enum
from typing import NewType

from pydantic import BaseModel, Field, constr, conint

from uuid import UUID, uuid4


class FilmCategory(str, Enum):
    ARTHOUSE = 'Артхаус'
    BIOGRAPHY = 'Біографічний'
    ACTION = 'Бойовик'
    DOCUMENTARY = 'Документальний'
    DRAMA = 'Драма'
    DETECTIVE = 'Детектив'
    HISTORICAL = 'Історичний'
    COMEDY = 'Комедія'
    CRIME = 'Кримінал'
    MELODRAMA = 'Мелодрама'
    MUSICAL = 'Мюзикл'
    ANIMATION = 'Мультфільм'
    THRILLER = 'Трилер'
    SCIENCE_FICTION = 'Фантастика'
    FANTASY = 'Фентезі'

class FilmBase(BaseModel):
    film_title: constr(min_length=2, max_length=20, pattern="^[ а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']*$")
    year: int = Field(..., gt=1900, lt=2500, description="Рік виходу фільму", example=1930)
    category: FilmCategory
    my_rate: conint(ge=0, le=10) = 0


class Film(FilmBase):
    id_4: int

    class Settings:
        orm_mode = True


class FilmCreate(FilmBase):
    pass


DBDict = NewType("DBDict", dict[UUID, Film])
