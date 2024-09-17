from fastapi  import FastAPI

app = FastAPI()

@app.get("/")
def test_root():
    return {"test": "passed_well"}

from typing import NewType

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, constr, conint

from uuid import UUID, uuid4

app = FastAPI()


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

films: DBDict = {}


@app.post("/films/", response_model=Film)
def create_film(film: Film):
    film.idu4 = uuid4()
    films[film.idu4] = film
    return film


@app.get("/films/", response_model=DBDict)
def read_films():
    return films


@app.get("/films/{film_id}", response_model=Film)
def read_task(film_id: UUID):
    if film_id in films:
        return films[film_id]

    raise HTTPException(
        status_code=404, detail=f"Фільм з ключем {film_id} не знайдено."
    )


@app.put("/films/{film_id}", response_model=Film)
def update_film(film_id: UUID, film_update: Film):
    if film_id in films:
        updated_film = films[film_id].model_copy(
            update=film_update.model_dump(exclude_unset=True)
        )
        films[film_id] = updated_film
        return updated_film

    raise HTTPException(
        status_code=404, detail=f"Фільм з ключем {film_id} не знайдено."
    )


@app.delete("/films/{film_id}", response_model=Film)
def delete_film(film_id: UUID):
    if film_id in films:
        return films.pop(film_id)

    raise HTTPException(
        status_code=404, detail=f"Фільм з ключем {film_id} не знайдено."
    )

