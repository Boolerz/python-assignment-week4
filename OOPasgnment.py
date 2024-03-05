class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"The book '{self.title}' has been checked out.")
        else:
            print(f"The book '{self.title}' is already checked out.")

    def check_in(self):
        if not self.is_available:
            self.is_available = True
            print(f"The book '{self.title}' has been checked in.")
        else:
            print(f"The book '{self.title}' is already checked in.")

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Available: {self.is_available}"

# Creating instances of the Book class
book1 = Book("Rich dad poor Dad", "Robert T. Kiyosaki", 1997)
book2 = Book("The Psychology of Money", "Morgan Housel", 2020)

# Checking out and checking in a book
book1.check_out()
book1.check_in()

# Printing information of both books
print("Book 1 Information:")
print(book1)
print("\nBook 2 Information:")
print(book2)
