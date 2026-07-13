class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print(f"You borrowed: {self.title}")

    def return_book(self):
        self.is_borrowed = False
        print(f"You returned: {self.title}")



# 1. Create 3 book objects
book1 = Book("Dog Man", "Dav Pilkey")
book2 = Book("Captain Underpants", "Dav Pilkey")
book3 = Book("To Kill a Mockingbird", "Lee")

# 2. Borrow books
book1.borrow()
book2.borrow()

# 3. Return books
book1.return_book()
book3.return_book()