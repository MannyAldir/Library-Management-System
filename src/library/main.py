from library import Library
from book import Book
from book_search_strategy import AuthorSearch, TitleSearch, IsbnSearch

if __name__ == "__main__":
    b1 = Book("J.K Rowling", "Harry Potter The Sorceror's Stone", 112233)
    b2 = Book("Victor Frankyl", "Man Search For Meaning", 982173)

    fauLibrary = Library()
    fauLibrary.add_book(b1)
    fauLibrary.add_book(b2)
    fauLibrary.check_out(b1)
    fauLibrary.check_status(b1)
    fauLibrary.set_strategy(AuthorSearch())
    frankyl_books = fauLibrary.search("Victor Frankyl")
    fauLibrary.set_strategy(IsbnSearch())
    jk_books = fauLibrary.search(112233)
    fauLibrary.set_strategy(TitleSearch())

    # print books
    for book in frankyl_books:
        print(book)
    for book in jk_books:
        print(book)
    print(fauLibrary.search("man search for meaning")[0])

    # dunder methods
    print(len(fauLibrary))
    print(next(iter(fauLibrary)))
    print(fauLibrary[0])
