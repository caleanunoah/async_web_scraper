import asyncio
import time
import aiohttp
import async_timeout
import requests

from pages.books_page import BooksPage


# Task - async function that we are defining below
async def fetch_page(session, url):
    start = time.time()
    async with async_timeout.timeout(30):
    # Note that instead of : __enter__ and __exit__
    # The methods are __aenter__ and __aexit__
        async with session.get(url) as response:
            print(f"Page took {time.time() - start}")
            return await response.text()


# Passing in event loop as an arg for safeguarding.
# Ensures that new loop isn't created every time
async def get_multiple_pages(loop, *urls):
    tasks = []
    async with aiohttp.ClientSession(loop=loop) as session:
        for url in urls:
            tasks.append(fetch_page(session, url))
        # Each task in grouped_tasks runs synchronously
        grouped_tasks = asyncio.gather(*tasks)  # runs until tasks are DONE.  All pages gathered
        return await grouped_tasks  # suspects after collecting all pages


URL = 'http://books.toscrape.com/catalogue/page-1.html'
content = requests.get(URL).content
page = BooksPage(content)

loop = asyncio.get_event_loop()
books = page.books

urls = [f'http://books.toscrape.com/catalogue/page-{page_num+1}.html' for page_num in range(page.page_count)]

start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))
print(f'total page requests took: {time.time()-start}')

for page_content in pages:
    page = BooksPage(page_content)
    books.extend(page.books)

'''
for page_num in range(1, page.page_count):
    print(page_num)
    url = f'http://books.toscrape.com/catalogue/page-{page_num+1}.html'
    page_content = requests.get(url).content
    #logger.debug("Creating BooksPage from page content")
    page = BooksPage(page_content)
    books.extend(page.books)
'''
