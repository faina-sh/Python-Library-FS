from book import Book
from reader import Reader
from shelf import Shelf


class Library:
    SHELF_NUM = 3

    def __init__(self):
        self.shelves: list[Shelf] = []
        self.readers: list[Reader] = []
        self._init_shelves()
        self.first_free_shelf_idx = 0

    def is_there_place_for_new_book(self) -> bool:
        for idx, shelf in enumerate(self.shelves):
            if not shelf.get_is_shelf_full():
                self.first_free_shelf_idx = idx
                return True
        self.first_free_shelf_idx = -1
        return False

    def add_new_book(self, book: Book) -> None:
        if not self.is_there_place_for_new_book():
            print("Can't add the book, there is no available space on any shelf")
            return
        self.shelves[self.first_free_shelf_idx].add_book(book=book)
        print("Book was added successfully")

    def delete_book(self, title: str):
        book_deleted = False
        for shelf in self.shelves:
            idx = shelf.find_book(title=title)
            if idx != -1:
                shelf.delete_book(index=idx)
                book_deleted = True
                print(f"{title} was deleted from shelf {idx}")
                break
        if not book_deleted:
            print(f"{title} is not in the inventory, deletion failed.")

    def register_reader(self, name: str, reader_id: int) -> None:
        for reader in self.readers:
            if reader.reader_id == reader_id:
                print(f"Cant add reader with reader_id: {reader_id} , reader_id exists.")
                return
        self.readers.append(Reader(reader_id, name))

    def remove_reader(self, name: str) -> None:
        reader_found = False
        for idx, reader in enumerate(self.readers):
            if reader.name.strip() == name.strip():
                reader_found = True
                break
        if not reader_found:
            print("Can't remove reader, reader name not found")
            return

        self.readers.pop(idx)
        print(f"The reader {name} was deleted successfully")

    def search_by_author(self, author: str) -> list:
        titles_by_author = []
        for shelf in self.shelves:
            for book in shelf.books:
                if book is None:
                    continue
                if book.author.strip() == author.strip():
                    titles_by_author.append(book.title)

        return titles_by_author

    def _init_shelves(self):
        self.shelves.append(Shelf([Book(author="F. Scott Fitzgerald", title="The Great Gatsby", num_of_pages=878),
                                   Book(author="George Orwell", title="1984", num_of_pages=576)])) 
        self.shelves.append(Shelf([Book(author="Jane Austen", title="Pride and Prejudice", num_of_pages=342),
                                   Book(author="Charlotte Bronte", title="Jane Eyre",num_of_pages=582)])) 
        self.shelves.append(Shelf([Book(author="J.K.Rowling", title="Harry Potter and the Half-Blood Prince", num_of_pages=1000),
             Book(author="Paulo Coelho", title="The Alchemist",num_of_pages=250)]))
