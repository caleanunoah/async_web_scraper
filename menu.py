from app import books

USER_PAGE = "Please enter a page to search (Press Enter for default -- First pg):  "
USER_CHOICE = """Enter one of the following

- 'b' to look at all 5-star books
- 'c' to look at the 5 cheapest books
- 'n' to get next available book in catalogue
- 'q' to quit
    
Enter your choice:  """

# Functions to filter the books based on user input


def sort_best_books():
    """
    :return: list of top 5 books by rating
    """
    best_books = sorted(books, key=lambda x: x.rating * -1)[:5]
    for book in best_books:
        print(book)


def sort_cheapest_books():
    """
    :return: List of top 5 cheapest books
    """
    cheap_books = sorted(books, key=lambda x: x.price)[:5]
    for book in cheap_books:
        print(book)


books_generator = (x for x in books)


def sort_next_available():
    """
    :return: list of available books
    """
    print(next(books_generator))


user_choices = {
    'b': sort_best_books,
    'c': sort_cheapest_books,
    'n': sort_next_available,
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        # More compact way
        if user_input in {'b', 'c', 'n'}:
            user_choices[user_input]()
        else:
            print("Please choose valid command.  ")
        user_input = input(USER_CHOICE)


if __name__ == '__main__':
    menu()
