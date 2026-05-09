from book import Book
from typing import Iterator


class Library:
    def __init__(self) -> None:
        self.book_list: list[Book] = [] 

    def __len__(self)->int:
        return len(self.book_list)
    
    def __iter__(self)->Iterator[Book]:
        return iter(self.book_list)
    
    def __getitem__(self,ind:int)->Book:
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

    def check_status(self, book:Book) -> None:
        if book.available:
            print(f"A copy of {book.title} by {book.author} is available for checkout.")
        else:
            print(f"There are no copies available of {book.title} by {book.author}")

    def search_book(self, author:str) -> list[Book]:
        books = []
        for book in self.book_list:
            if book.author.lower() == author.lower():
                books.append(book)
        return books
