import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")  # (la clave está en .env)
    BASE_URL = "https://api.themoviedb.org/3"