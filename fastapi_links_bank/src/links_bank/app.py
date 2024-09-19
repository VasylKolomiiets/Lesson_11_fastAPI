from fastapi  import FastAPI
from fastapi import FastAPI, HTTPException
from .api import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def test_root():
    return {"test": "passed_well"}

from .models.films import Film, DBDict, uuid4, UUID

films: DBDict = {}


# @app.post("/films/", response_model=Film)
# def create_film(film: Film):
#     film.idu4 = uuid4()
#     films[film.idu4] = film
#     return film


# @app.get("/films/", response_model=DBDict)
# def read_films():
#     return films


@app.get("/films/{film_id}", response_model=Film)
def read_film(film_id: UUID):
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

