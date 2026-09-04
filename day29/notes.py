'''
Request:
--------
--> Request module is used to send the HTTP request to the server 

Beautiful module:
-----------------
--> bs4 is version of the module, which is used to get the data from website

Popular Libraries:
------------------
Library	                 Purpose
Requests	    Fetch HTML content from URLs
BeautifulSoup	Parse and extract data from HTML
Selenium	    Automate browser interactions (JavaScript)
Scrapy	        Full-featured scraping framework
lxml	        Fast XML/HTML parsing

Installation:
-------------
pip install requests beautifulsoup4 selenium lxml

Web Scraping:
-------------
--> The process of collecting data from the website with normal python program is called as web scraping

Task	            Code
Fetch page	    requests.get(url)
Parse HTML	    BeautifulSoup(content, 'html.parser')
Find one	    soup.find('tag', class_='name')
Find all	    soup.find_all('tag')
Get text	    .get_text()
Get attribute	.get('attr') or ['attr']
CSS selector	soup.select('.class')
Next sibling	.find_next_sibling()
Parent	        .parent

example:
--------
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the webpage
url = "https://example.com"
response = requests.get(url)

# Step 2: Check if request was successful
if response.status_code == 200:
    print("Success!")
else:
    print(f"Error: {response.status_code}")

# Step 3: Parse the HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Step 4: Extract data
title = soup.title.string
print(f"Page Title: {title}")
------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'
response = requests.get(url)
print(response.status_code)
title = BeautifulSoup(response.text,'html.parser')
books = title.find_all('h3')
for book in books:
    title = book.find('a').get('title')
    print(title)

'''