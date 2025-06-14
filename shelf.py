from book import Book
from typing import List


class Shelf:
    CAPACITY = 5

    def __init__(self, predefined_books: List) -> None:
        if len(predefined_books) >= Shelf.CAPACITY:
            self.books: Book = predefined_books[:Shelf.CAPACITY]
            self.is_shelf_full: bool = True
        else:
            self.books: list = predefined_books + [None] * (5 - len(predefined_books))
            self.is_shelf_full: bool = False

    def add_book(self, book: Book):
        if book is None:
            print("You Must pass a valid book")
            return
        if self.is_shelf_full:
            print("Can't add a book to the shelf, the shelf full")
            return

        first_empty_index = self.books.index(None)
        self.books[first_empty_index] = book

        if None not in self.books:
            self.set_is_shelf_full(True)

    def replace_books(self, pos1: int, pos2: int):
        pos1 -= 1
        pos2 -= 1

        if not (0 <= pos1 < Shelf.CAPACITY and 0 <= pos2 < Shelf.CAPACITY):
            print("Positions for replacement are invalid (must be between 1-5)")
            return

        if self.books[pos1] is None or self.books[pos2] is None:
            print("One of the indices is empty - can't replace")
            return

        self.books[pos1], self.books[pos2] = self.books[pos2], self.books[pos1]

    def remove_book(self, book: Book):
        book_index = self.books.index(book)
        self.books[book_index] = None

    def set_is_shelf_full(self, is_full: bool):
        self.is_shelf_full = is_full

    def get_is_shelf_full(self) -> bool:
        return self.is_shelf_full

    def find_book(self, title: str) -> int:
        for idx, book in enumerate(self.books):
            if book is None:
                continue
            if title.strip() == book.title.strip():
                return idx
        return -1

    def delete_book(self, index: int):
        # is called only if the book was already found so index is valid
        self.books[index] = None
        self.set_is_shelf_full(False)
