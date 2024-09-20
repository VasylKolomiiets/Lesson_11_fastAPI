from fastapi  import FastAPI
from .api import router

app = FastAPI(
    prefix='ФільмиУ'
)
app.include_router(router)

@app.get("/")
def test_root():
    return {"test": "passed_well"}
