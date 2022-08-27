from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movie_page = response.text
soup = BeautifulSoup(movie_page, "html.parser")

titles_tags = soup.find_all("h3", class_="title")
file = open("movie.txt", "a", encoding="utf8")
for tag in titles_tags:
    tag = tag.getText()
    try:
        rank = int(tag.split(")")[0])
    except ValueError:
        rank = int(tag.split(":")[0])
        title = tag.split(":")[1]
    else:
        title = tag.split(")")[1]
    finally:
        file.write(f"{rank}) {title}\n")

file.close()
