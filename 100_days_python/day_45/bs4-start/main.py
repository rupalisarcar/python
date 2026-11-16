from bs4 import BeautifulSoup
import requests

# This code will fetch data from the static practice website that I've created for you:
response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.find_all(name="a", class_="storylink")
article_link = []
article_text = []

for article in article_tag : 
    article_text.append(article.getText())
    article_link.append(article.get("href"))
print(article_link)
article_upvotes = soup.find_all(name="span", class_="score")
upvotes = [int(item.getText().split(' ')[0]) for item in article_upvotes]

largest_upvote = max(upvotes)
index = upvotes.index(largest_upvote)
text = article_text[index]
link = article_link[index]

print(text)
print(link)
# file_path = "D:/python/100_days_python/day_45/bs4-start/website.html"
# with open(file_path,'r') as html_file:
#     contents = html_file.read()
#     print(contents)