class Library:
    def __init__(self):
        self.books = []   # List to store available books

    def add_book(self, book_name):
        if book_name not in self.books:
            self.books.append(book_name)
            print(f'"{book_name}" added successfully.')
        else:
            print(f'"{book_name}" already exists.')

    def issue_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f'"{book_name}" issued successfully.')
        else:
            print(f'"{book_name}" is not available.')

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f'"{book_name}" returned successfully.')

    def show_books(self):
        if self.books:
            print("Available books:")
            for book in self.books:
                print("-", book)
        else:
            print("No books available.")



lib = Library()

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Show Available Books")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        book = input("Enter book name to add: ")
        lib.add_book(book)
    elif choice == "2":
        book = input("Enter book name to issue: ")
        lib.issue_book(book)
    elif choice == "3":
        book = input("Enter book name to return: ")
        lib.return_book(book)
    elif choice == "4":
        lib.show_books()
    elif choice == "5":
        print("Exiting Library... Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1-5.")
