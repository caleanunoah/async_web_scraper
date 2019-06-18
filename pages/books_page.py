from bs4 import BeautifulSoup
from parsers.books import BooksParser
from locators.books_page_locators import BooksPageLocators
import re
import logging

logger = logging.getLogger("scraping.books_page")


class BooksPage:
    """
    Takes in front page and extracts information
    """
    def __init__(self, page):
        logger.debug("Parsing page content with BeautifulSoup")
        self.soup = BeautifulSoup(page, 'html.parser')

    """
    Organizes the books into a list.
    """
    @property
    def books(self):
        logger.debug("Getting all books on page")
        book_info = self.soup.find_all('article', attrs={'class': 'product_pod'})
        return [BooksParser(b) for b in book_info]

    """
    From current page find the next page.
    """
    @property
    def next(self):
        next_page_locator = 'div.page_inner section div div ul.pager li.next a'
        next_page = self.soup.select_one(next_page_locator).attrs['href']
        return next_page

    @property
    def page_count(self):
        logger.debug("Finding all number of catalogue pages available.")
        content = self.soup.select_one(BooksPageLocators.PAGER).string.strip()
        logger.info(f"Found number of catalogue pages available: `{content}` ")
        pattern = ' '
        return int(re.split(pattern, content)[3])
