from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Server is working 🔥"}

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")