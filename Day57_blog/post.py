import requests

class Post:
    def __init__(self, url):
        self.url = url

    def get_posts(self):
        posts = requests.get(self.url).json()
        print(posts)
        return posts
