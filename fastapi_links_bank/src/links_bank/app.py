from fastapi  import FastAPI

from .app import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def test_root():
    return {"test": "passed_well"}


