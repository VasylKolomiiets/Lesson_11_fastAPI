"""Класи-моделі, що використовуються для сутності `фільми`."""
from pydantic import BaseModel


from typing import NewType

from pydantic import BaseModel, Field, constr, conint

from uuid import UUID, uuid4


class Film(BaseModel):
    idu4: UUID | None = None
    film_title: constr(
        min_length=2, max_length=20, pattern="^[ а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']*$"
    )
    year: int = Field(
        ..., gt=1900, lt=2500, description="Рік виходу фільму", example=1930
    )
    category: constr(min_length=4, max_length=20)
    my_rate: conint(ge=0, le=10) = 0


DBDict = NewType("DBDict", dict[UUID, Film])
