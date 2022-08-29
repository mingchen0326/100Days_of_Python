from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import requests
import spotipy
import os

# ----------------------------------Get top 100 songs on the date input by user----------------------
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date = "2000-08-26"
web_url = f"https://www.billboard.com/charts/hot-100/{date}"
response = requests.get(web_url)

web_content = response.text

soup = BeautifulSoup(web_content, "html.parser")

li_tag = soup.find_all(name="li", class_="lrv-u-width-100p")
li_tag = [li_tag[i] for i in range(len(li_tag)) if i % 2 == 0]

index = 0
# for tag in li_tag:
#     title = tag.find(name="h3").getText()
#     title = "".join(title.split())
#     index += 1
#     print(f"------------------------------------------\n"
#           f"{index}: {title}")
#
#     artist = tag.find(name="span").getText()
#     artist = "".join(artist.split())
#     print(f"------------------------------------------\n"
#           f"{index}: {artist}")

# ----------------------------------use Spotipy to access Spotify user account----------------------
client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")
username = os.environ.get("SPOTIFY_USERNAME")
redirect_uri = "http://example.com"
print(client_id)
print(client_secret)
print(username)

response = spotipy.oauth2.SpotifyOAuth(scope="playlist-modify-private",
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri,
                                       username=username,
                                       show_dialog=True,
                                       open_browser=False,
                                       cache_path="token.txt")
response.get_auth_response()

