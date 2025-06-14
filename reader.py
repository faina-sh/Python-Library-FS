class Reader:
    def __init__(self, reader_id: int, name: str):
        self.reader_id: int = reader_id
        self.name: str = name
        self.books_read: list = []

    def read_book(self, title: str):
        if title.strip() in self.books_read:
            print(f"{self.name} has already read {title} before.")
        else:
            self.books_read.append(title.strip())
            print(f"{self.name} read {title}!")