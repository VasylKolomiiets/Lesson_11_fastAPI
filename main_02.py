from typing import Alias

from fastapi import FastAPI
from pydantic import BaseModel, Field, constr, conint

from uuid import UUID, uuid4

app = FastAPI()

DBDict: Alias = 'dict[uuid4, Film]'

class Film(BaseModel):
    film_title: constr(min_length=2, max_length=20, pattern="^[ а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']*$")
    year: int = Field(..., gt=1900, lt=2500, description="Рік виходу фільму", example=1930)
    category: constr(min_length=5, max_length=20)
    my_rate: conint(ge=0, le=10)



films: dict[uuid4, Film] = {}

@app.post("/tasks/", response_model=Film)
def create_task(task: Film):
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/filmss/", response_model=dict[Task])
def read_tasks():
    return tasks


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000) # host="0.0.0.0", 

from fastapi import FastAPI
from pydantic import BaseModel, Field, constr, conint

from uuid import UUID, uuid4

app = FastAPI()

DBDict: Alias = 'dict[uuid4, Film]'

class Film(BaseModel):
    film_title: constr(min_length=2, max_length=20, pattern="^[ а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']*$")
    year: int = Field(..., gt=1900, lt=2500, description="Рік виходу фільму", example=1930)
    category: constr(min_length=5, max_length=20)
    my_rate: conint(ge=0, le=10)



films: dict[uuid4, Film] = {}

@app.post("/tasks/", response_model=Film)
def create_task(task: Film):
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/filmss/", response_model=dict[Task])
def read_tasks():
    return tasks


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000) # host="0.0.0.0", 

from fastapi import FastAPI
from pydantic import BaseModel, Field, constr, conint

from uuid import UUID, uuid4

app = FastAPI()

DBDict: Alias = 'dict[uuid4, Film]'

class Film(BaseModel):
    film_title: constr(min_length=2, max_length=20, pattern="^[ а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']*$")
    year: int = Field(..., gt=1900, lt=2500, description="Рік виходу фільму", example=1930)
    category: constr(min_length=5, max_length=20)
    my_rate: conint(ge=0, le=10)



films: dict[uuid4, Film] = {}

@app.post("/tasks/", response_model=Film)
def create_task(task: Film):
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/filmss/", response_model=dict[Task])
def read_tasks():
    return tasks


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000) # host="0.0.0.0", 

from fastapi import FastAPI
from pydantic import BaseModel, Field, constr, conint

from uuid import UUID, uuid4

app = FastAPI()

DBDict: Alias = "dict[uuid4, Film]"

class Film(BaseModel):
    film_title: constr(min_length=2, max_length=20, pattern="^[ а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']*$")
    year: int = Field(..., gt=1900, lt=2500, description="Рік виходу фільму", example=1930)
    category: constr(min_length=5, max_length=20)
    my_rate: conint(ge=0, le=10)



films: dict[uuid4, Film] = {}

@app.post("/tasks/", response_model=Film)
def create_task(task: Film):
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/filmss/", response_model=dict[Task])
def read_tasks():
    return tasks


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000) # host="0.0.0.0", 

from fastapi import FastAPI
from pydantic import BaseModel, Field, constr, conint

from uuid import UUID, uuid4

app = FastAPI()

DBDict: Alias = "dict[uuid4, Film]"

class Film(BaseModel):
    film_title: constr(min_length=2, max_length=20, pattern="^[ а-щА-ЩЬьЮюЯяЇїІіЄєҐґ']*$")
    year: int = Field(..., gt=1900, lt=2500, description="Рік виходу фільму", example=1930)
    category: constr(min_length=5, max_length=20)
    my_rate: conint(ge=0, le=10)



films: dict[uuid4, Film] = {}

@app.post("/tasks/", response_model=Film)
def create_task(task: Film):
    task.id = uuid4()
    tasks.append(task)
    return task


@app.get("/filmss/", response_model=dict[Task])
def read_tasks():
    return tasks


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8000) # host="0.0.0.0", 