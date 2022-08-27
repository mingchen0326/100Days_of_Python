# import lxml
#
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title.string)
#
# all_anchor_tag = soup.find_all(name="a")
#
#
# for tag in all_anchor_tag:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
