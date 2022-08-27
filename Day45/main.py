from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag = soup.find(name="a", class_="titlelink")
# print(article_tag)
# article_link = article_tag.get("href")
# print(article_link)
# score_tag = soup.find(name="span", class_="score")
# print(score_tag.getText())
dict = {}
all_anchor_tag = soup.find_all(name="a", class_="titlelink")
all_span_tag = soup.find_all(name="span", class_="score")
# for index in range(len(all_anchor_tag)):
#     anchor_tag = all_anchor_tag[index]
#     span_tag = all_span_tag[index]
#     key = f"tag{index+1}"
#     article_title = anchor_tag.getText()
#     article_link = anchor_tag.get("href")
#     article_upvote = span_tag.getText()
#     dict[key] = {"article_title": article_title,
#                  "article_link": article_link,
#                  "article_upvote": article_upvote}
index = 0
max_vote = -1
max_vote_tag = ""
for anchor_tag, span_tag in zip(all_anchor_tag, all_span_tag):
    index += 1
    key = f"tag{index}"
    article_title = anchor_tag.getText()
    article_link = anchor_tag.get("href")
    article_upvote = span_tag.getText()
    vote = article_upvote.split(" ")[0]
    print(vote)
    if int(vote) > max_vote:
        max_vote = int(vote)
        max_vote_tag = key
    dict[key] = {"article_title": article_title,
                 "article_link": article_link,
                 "article_upvote": article_upvote}

print(max_vote)
print(max_vote_tag)
print(dict)