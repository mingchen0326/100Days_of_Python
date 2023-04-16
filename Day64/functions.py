import requests

api_key = "7b02ed935169bf5779f6ee5e140ba65b"


def get_movie(title):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&language=en-US&query={title}&include_adult=false"
    movies = requests.get(url).json()["results"]
    for movie in movies:
        if movie["original_title"] == title:
            result = {'title': movie["original_title"],
                      'year': movie["release_date"][:4],
                      'description': movie["overview"],
                      'rating': round(movie["vote_average"], 1),
                      'ranking': 0,
                      'review': "N/A",
                      'img_url': f"https://image.tmdb.org/t/p/w600_and_h900_bestv2{movie['poster_path']}"}
            return result

