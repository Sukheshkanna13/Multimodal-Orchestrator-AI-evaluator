from fastapi import FastAPI
from src.api.v1.router import router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the SASES API"}

app.include_router(router, prefix="/api/v1")