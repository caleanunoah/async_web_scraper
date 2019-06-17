import requests
from pages.books_page import BooksPage

"""
URL = 'http://books.toscrape.com'
URL_NEXT = 'http://books.toscrape.com/catalogue/page-'+str(2)+'.html'

content = requests.get(URL_NEXT).content
page = BooksPage(content)

books = page.books
max_pages = page.scroll  # this is an int
"""

page_collection = []

print("\n STARTING ......................................................")
for i in range(1, 5):
    print("i = ", i)
    URL = 'http://books.toscrape.com/catalogue/page-'+str(i)+'.html'
    content = requests.get(URL).content
    page = BooksPage(content)
    new_book = page.books
    page_collection.append(new_book)



print(books)
