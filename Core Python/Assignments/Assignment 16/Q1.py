class Book:
    count = 0  # static variable

    def __init__(self, bid=0, bname="", price=0.0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
        print("Book object created")

    def __del__(self):
        print(f"Book object for '{self.bname}' destroyed")

    def ShowBook(self):
        print("----- Book Details -----")
        print("Book ID    :", self.bid)
        print("Book Name  :", self.bname)
        print("Price      :", self.price)
        print("Author     :", self.author)


b1 = Book(101, "Python Programming", 450.0, "John Smith")
b2 = Book(102, "Data Structures", 350.0, "Alice Brown")
print("Total Books created:", Book.count)