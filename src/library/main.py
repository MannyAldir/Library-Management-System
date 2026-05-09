from library import Library
from book import Book

if __name__ == "__main__":
    b1 = Book("J.K Rowling", "Harry Potter The Sorceror's Stone", 112233)
    b2 = Book("Victor Frankyl", "Man Search For Meaning", 982173)

    fauLibrary = Library()
    fauLibrary.add_book(b1)
    fauLibrary.add_book(b2)
    fauLibrary.check_out(b1)
    fauLibrary.check_status(b1)
    frankyl_books = fauLibrary.search_book("Victor Frankyl")
    for book in frankyl_books:
        print(book)
    print(fauLibrary.__len__())
    print(next(fauLibrary.__iter__()))
    print(fauLibrary.__getitem__(1))
