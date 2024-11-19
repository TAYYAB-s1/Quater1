class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = [
            Book("To Kill a Mockingbird", "Harper Lee"),
            Book("1984", "George Orwell"),
            Book("The Great Gatsby", "F. Scott Fitzgerald")
        ]
        self.users = [User(1)]

    def display_all_books(self):
        print("All Books:")
        for i, book in enumerate(self.books):
            print(f"{i+1}. {book.title} by {book.author} ({'Available' if book.available else 'Checked Out'})")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def borrow_book(self, user_id, book_id):
        user = self.find_user_by_id(user_id)
        book = self.books[book_id - 1]
        if book.available:
            book.available = False
            user.borrowed_books.append(book)
            print(f"You have successfully borrowed the book '{book.title}'.")
        else:
            print("Sorry, the book is currently checked out.")

    def return_book(self, user_id, book_id):
        user = self.find_user_by_id(user_id)
        book = self.books[book_id - 1]
        if book in user.borrowed_books:
            book.available = True
            user.borrowed_books.remove(book)
            print(f"You have successfully returned the book '{book.title}'.")
        else:
            print("You do not have this book checked out.")

    def view_all_users(self):
        print("All Users:")
        for user in self.users:
            print(f"User ID: {user.user_id}")

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

def main():
    library = Library()

    while True:
        print("Welcome to the Community Library System!")
        print("----------------------------------------")
        print("Please choose an option:")
        print("1. View all books")
        print("2. Search for a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all users")
        print("6. Exit")
        print("Enter your choice (1-6): ", end="")
        choice = int(input())

        if choice == 1:
            library.display_all_books()
        elif choice == 2:
            title = input("Enter the book title: ")
            book = library.search_book(title)
            if book:
                print(f"Book Found: {book.title} by {book.author}")
            else:
                print("Book not found.")
        elif choice == 3:
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to borrow: "))
            library.borrow_book(user_id, book_id)
        elif choice == 4:
            user_id = int(input("Enter your User ID: "))
            book_id = int(input("Enter the Book ID you want to return: "))
            library.return_book(user_id, book_id)
        elif choice == 5:
            library.view_all_users()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()