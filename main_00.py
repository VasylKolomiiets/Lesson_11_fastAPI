from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
def easy_start():
    return {"film_title": "Довбуш", "year": 2023}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, port=8000) # host="0.0.0.0",
