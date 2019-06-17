import requests
import logging

from pages.books_page import BooksPage

logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    level=logging.DEBUG,
                    filename='logs.txt')

logger = logging.getLogger('scraping')

logger.info("Loading books list...")

URL = 'http://books.toscrape.com/catalogue/page-1.html'
content = requests.get(URL).content
page = BooksPage(content)

books = page.books

for page_num in range(1, page.page_count):
    print(page_num)
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    logger.debug("Creating BooksPage from page content")
    page = BooksPage(page_content)
    books.extend(page.books)


# MY OWN IMPLEMENTATION DOING THE SAME THING BUT MORE COMPLICATED RIPPPPp

"""
URL = [0, 'http://books.toscrape.com']

content = requests.get(URL[1]).content
page = BooksPage(content)
books = page.books
next_page = page.next  # this is a link
URL.append('http://books.toscrape.com/'+next_page)

print(books)
print(URL)
print("STARTING -------------------")

for i in range(2, 50):
    print(i)
    print("\n_______________________________________________________________________________________")
    content = requests.get(URL[i]).content
    page = BooksPage(content)
    books = page.books
    next_page = page.next  # this is a link
    URL.append('http://books.toscrape.com/catalogue/' + next_page)
    print("For this iteration: ", URL)
    print(books)
"""

