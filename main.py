from book import Book
from reader import Reader
from shelf import Shelf
from library import Library


def library_manager():
    library = Library()

    while True:
        for i, shelf in enumerate(library.shelves):
            print(f"\nShelf #{i+1}: [", end="")

            for k,book in enumerate(shelf.books):
                if book is None:
                    print("None", end="")
                    if k < len(shelf.books)-1:
                        print(",", end="") 
                    continue
                print(book.title, end="")

                if k < len(shelf.books)-1:
                    print(",", end="") 

            print(f"]\nShelf #{i+1} is full: {shelf.is_shelf_full}")

        print(f"\nLibrary readers: ")
        for reader in library.readers:
            print(reader.name)
        print('\n')

        print("***Library Menu***")
        print("To add a book - Press 1")
        print("To delete a book - Press 2")
        print("To register a new reader - Press 3")
        print("To remove a reader - Press 4")
        print("To search books by author – Press 5")
        print("To exit - Press 6\n")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nYou chose to add a book")
            author = input("Enter the author's name: ")
            if not author:
                print("Invalid author's name")
                continue
            title = input("Enter the title name: ")
            if not title:
                print("Invalid title name")
                continue
            num_of_pages = input("Enter the number of pages: ")
            if not num_of_pages.isdigit() or int(num_of_pages) <= 0:
                print("Number of pages must be a valid positive integer.Book was not added.")
                continue

            num_of_pages = int(num_of_pages)
            new_book = Book(author=author, title=title, num_of_pages=num_of_pages)
            library.add_new_book(new_book)

        elif choice == '2':
            title = input("Enter the title of the book to delete: ").strip()
            if title:
                library.delete_book(title)
            else:
                print("Invalid title.")

            
        elif choice == '3':
            print("You chose to register a new reader.")
            name = input("Enter the reader's name: ")
            if not name:
                print("Invalid reader's name")
                continue
            id = input("Enter the reader's id: ")
            if not id.isdigit() or int(id) <= 0:
                print("The id must be a valid positive integer.")
                continue
            id = int(id)
            library.register_reader(name=name, reader_id=id)

        elif choice == '4':
            print("You chose to remove a reader.")
            name = input("Enter the reader's name: ")
            if not name:
                print("Invalid reader's name")
                continue
            library.remove_reader(name=name)

        elif choice == '5':
            print("You chose to search books by author.")
            name = input("Enter the author's name: ")
            if not name:
                print("Invalid author's name")
                continue
            titles_by_author = library.search_by_author(author=name)
            print(f"Books by {name} : {titles_by_author}")

        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    library_manager()
