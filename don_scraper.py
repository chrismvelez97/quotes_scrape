                        # Guide To Web Scraping(Python3
# To web scrape we will use the beautifulSoup4 module
from bs4 import BeautifulSoup as bs

# Here we'll import requests so we can make url requests
import requests

# Here we'll use json to store our scraped data
import json

# Here we'll grab the source code for the website we want to scrape
source = requests.get('http://quotes.toscrape.com/').text

# print (source)  This shows we have the html document

'''
When we imported BeautifulSoup, we gave the function an alias called bs, which
is how we're accessing the function below.

The BeautifulSoup function takes in two arguments, the first of which is,
the source code for the website.

The second argument is the parser we want to use.  There are multiple parsers,
and even python has a built in parser but for this example we'll use lxml.
'''
soup = bs(source, 'lxml')

# print (soup.prettify()) Again shows we have the html document

'''
This code below grabs the specific quote we'd like to grab the html for.
The first argument 'div' is to find the div element.  The second argument
is to narrow our search down even further to the class quote.

It should be noted that we typed class_ with an underscore but this is only
because class is already a keyword within python.
'''
book_of_quotes = {}
for div in soup.find_all('div', class_='quote'):

    # Here we've grabbed the author for the quote we'd like
    # The next_sibling attribute is a way for us to grab sibling
    # elements on a page since there were multiple span elements
    author = div.span.next_sibling.next_sibling.small.text

    # Here we've grabbed the text for the quote we'd like
    quote = div.span.text

    book_of_quotes[author] = quote

path = '/home/cvelez/Downloads/dump.json'
with open(path, 'w') as f_object:
    json.dump(book_of_quotes, f_object)
