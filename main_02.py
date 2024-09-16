from typing import NewType

from fastapi import FastAPI
from pydantic import BaseModel, Field, constr, conint

from uuid import UUID, uuid4

app = FastAPI()


class Film(BaseModel):
    idu4: UUID | None = None
    film_title: constr(min_length=2, max_length=20, pattern="^[ а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']*$")
    year: int = Field(..., gt=1900, lt=2500, description="Рік виходу фільму", example=1930)
    category: constr(min_length=4, max_length=20)
    my_rate: conint(ge=0, le=10) = 0

DBDict = NewType('DBDict', dict[UUID, Film]) 

films: DBDict = {}

@app.post("/films/", response_model=Film)
def create_film(film: Film):
    film.idu4 = uuid4()
    films[film.idu4] = film
    return film


@app.get("/films/", response_model=DBDict)
def read_films():
    return films


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)