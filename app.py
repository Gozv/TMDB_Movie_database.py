import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
import requests

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv('TMDB_API_KEY')
BASE_URL = "https://api.themoviedb.org/3"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search_movies():
    query = request.args.get('query')
    if not query:
        return render_template('index.html', error="Por favor ingresa un término de búsqueda")
    
    url = f"{BASE_URL}/search/movie"
    params = {
        'api_key': API_KEY,
        'query': query,
        'language': 'es-ES'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return render_template('search_results.html', results=data['results'], query=query)
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error=str(e))

@app.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        'api_key': API_KEY,
        'language': 'es-ES',
        'append_to_response': 'credits,recommendations'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        movie = response.json()
        return render_template('movie_details.html', movie=movie)
    except requests.exceptions.RequestException as e:
        return render_template('error.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)