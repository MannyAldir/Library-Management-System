from abc import ABC, abstractmethod
from book import Book


class BookSearchStrategy(ABC):
    @abstractmethod
    def search_book(self, query, bookList: list[Book]) -> list[Book]:
        pass


class TitleSearch(BookSearchStrategy):
    def search_book(self, query, bookList: list[Book]) -> list[Book]:

        return [book for book in bookList if query.lower() in book.title.lower()]


class AuthorSearch(BookSearchStrategy):
    def search_book(self, query, bookList: list[Book]) -> list[Book]:

        return [book for book in bookList if query.lower() in book.author.lower()]


class IsbnSearch(BookSearchStrategy):
    def search_book(self, query, bookList: list[Book]) -> list[Book]:

        return [book for book in bookList if query == book.isbn]
