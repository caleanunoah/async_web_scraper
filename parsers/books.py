import re
from locators.books_locators import BookLocators


class BooksParser:
    """
    Goes through each book found on page and extracts title, rating, and price information
    """
    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5

    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'{self.title}.\n{self.link}\n{self.rating}/5 stars.\nPriced at £{self.price}\n'

    @property
    def title(self):
        return self.parent.select_one(BookLocators.title_locator).attrs['title']

    @property
    def link(self):
        return self.parent.select_one(BookLocators.link_locator).attrs['href']

    @property
    def rating(self):
        list = self.parent.select_one(BookLocators.rating_locator)
        rating_cls = [cls for cls in list.attrs['class'] if cls != 'star-rating']
        rating = BooksParser.RATINGS.get(rating_cls[0], "N/A")     # None if not found
        return rating

    @property
    def price(self):
        price = self.parent.select_one(BookLocators.price_locator).string
        pattern = '£'
        return float(re.sub(pattern, "", price))




