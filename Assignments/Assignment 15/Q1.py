class Book:
    def __init__(self, bid=0, bname="", price=0.0, author=""):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print("Book object created")

    def __del__(self):
        print(f"Book object for '{self.bname}' destroyed")

    def ShowBook(self):
        print("----- Book Details -----")
        print("Book ID    :", self.bid)
        print("Book Name  :", self.bname)
        print("Price      :", self.price)
        print("Author     :", self.author)


b1 = Book()
b1.ShowBook()

b2 = Book(101, "Python Programming", 450.0, "John Smith")
b2.ShowBook()