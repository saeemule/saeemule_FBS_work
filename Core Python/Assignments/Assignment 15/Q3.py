class Shirt:
    def __init__(self, sid=0, sname="", type="", price=0.0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        print("Shirt object created")

    def __del__(self):
        print(f"Shirt object for '{self.sname}' destroyed")

    def ShowBook(self):
        print("----- Shirt Details -----")
        print("Shirt ID   :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type       :", self.type)
        print("Price      :", self.price)
        print("Size       :", self.size)


s1 = Shirt()
s1.ShowBook()

s2 = Shirt(301, "Formal Shirt", "Formal", 999.0, "Large")
s2.ShowBook()