from bs4 import BeautifulSoup
from parsers.books import BooksParser


class BooksPage:
    """
    Takes in front page and extracts information
    """
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    """
    Organizes the books into a list.
    """
    @property
    def books(self):
        book_info = self.soup.find_all('article', attrs={'class': 'product_pod'})
        return [BooksParser(b) for b in book_info]

    """
    From front page, deduces how many pages a user can have (assume at least one page exists)
    """
    @property
    def scroll(self):
        page_locator = 'div.container-fluid div.page_inner div.col-sm-8.col-md-9 form.form-horizontal strong'
        max = int(self.soup.select(page_locator)[2].string)
        return max
