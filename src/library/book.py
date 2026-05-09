class Book:
    def __init__(self, author: str, title: str, isbn: int, available:bool =True):
        self._author = author
        self._title = title
        self._isbn = isbn
        self.available = available

    @property
    def author(self) -> str:
        return self._author

    @property
    def title(self) -> str:
        return self._title.title()

    @property
    def isbn(self) -> int:
        return self._isbn

    def __repr__(self) -> str:
        status = "Available" if self.available else "checked out"
        return f"{self.title} by {self.author} is {status}"
