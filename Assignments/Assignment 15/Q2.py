class Product:
    def __init__(self, pid=0, pname="", price=0.0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        print("Product object created")

    def __del__(self):
        print(f"Product object for '{self.pname}' destroyed")

    def ShowBook(self):
        print("----- Product Details -----")
        print("Product ID  :", self.pid)
        print("Product Name:", self.pname)
        print("Price       :", self.price)
        print("Quantity    :", self.quantity)


p1 = Product()
p1.ShowBook()

p2 = Product(201, "Laptop", 55000.0, 10)
p2.ShowBook()