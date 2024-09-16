from fastapi import FastAPI
from pydantic import BaseModel, Field, constr

app = FastAPI()


class Film(BaseModel):
    film_title: constr(
        min_length=2, max_length=20, 
        pattern="^[ а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']*$",
    )
    year: int = Field(..., gt=1900, lt=2500, description="Рік виходу фільму", example=1930)


@app.get("/", response_model=Film)
def easy_start():
    return Film(film_title="Довбуш", year=2023)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000)
