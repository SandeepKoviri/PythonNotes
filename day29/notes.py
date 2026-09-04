import requests

from bs4 import BeautifulSoup

url_ = "https://books.toscrape.com/"
response = requests.get(url_)
title_ = BeautifulSoup(response.text, "html.parser")
books = title_.find_all('h3')

print(title_.title)
for book in books:
    title_ = book.find('a').get('title')
    print(title_)
    
