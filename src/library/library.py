from book import Book
from typing import Iterator
from book_search_strategy import BookSearchStrategy
from typing import Union


class Library:
    def __init__(self) -> None:
        self.book_list: list[Book] = []
        self._strategy = None

    def __len__(self) -> int:
        return len(self.book_list)

    def __iter__(self) -> Iterator[Book]:
        return iter(self.book_list)

    def __getitem__(self, ind: int) -> Book:
        return self.book_list[ind]

    def return_book(self, book: Book) -> None:
        if not book.available:
            book.available = True
            print(f"{book.title} returned")

    def check_out(self, book: Book) -> None:
        if book.available:
            book.available = False
            print(f"Checking out {book.title} by {book.author}")

    def add_book(self, book: Book) -> None:
        self.book_list.append(book)
        print(f"{book.title} added to library")

    def check_status(self, book: Book) -> None:
        if book.available:
            print(f"A copy of {book.title} by {book.author} is available for checkout.")
        else:
            print(f"There are no copies available of {book.title} by {book.author}")

    def set_strategy(self, strategy: BookSearchStrategy) -> None:
        self._strategy = strategy

    def search(self, query: Union[str, int]) -> list[Book]:
        if self._strategy:
            return self._strategy.search_book(query, self.book_list)
        print("No strategy set")
        return []
