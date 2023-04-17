import requests
from movie_class import Movie

api_key = "7b02ed935169bf5779f6ee5e140ba65b"


def search_movie(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={title}&include_adult=false"
    movies = requests.get(url).json()["results"]
    return movies
    # for movie in movies:
    #     print(f"{movie['original_title']} - {movie['release_date']}")


def get_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    result = requests.get(url).json()
    target_movie = Movie()
    target_movie.id = movie_id
    # print(type(target_movie.id), target_movie.id)
    target_movie.title = result['original_title']
    target_movie.year = result['release_date'][:4]
    target_movie.description = result['overview']
    target_movie.rating = round(result['vote_average'], 1)
    target_movie.ranking = 0
    target_movie.review = result['tagline']
    target_movie.img_url = f"https://image.tmdb.org/t/p/w500{result['poster_path']}"
    return target_movie

