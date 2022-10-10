from fastapi import FastAPI
import coldStart as cs
import contentBased as cb
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()

origins = [
    "http://localhost:3333",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Movie(BaseModel):
    movie_name: str

@app.get("/ping")
async def start():
    return "pong"

@app.get("/cold_start")
async def coldStart():
    return cs.topMovies()
# uvicorn main:app --reload

@app.post("/content_based/")
async def contentBased(movie_name: Movie):
    print(movie_name.movie_name)
    return cb.wantedMovie(movie_name.movie_name)