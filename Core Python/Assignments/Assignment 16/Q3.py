class Shirt:
    size_factor = {"small": 1.0, "medium": 1.1, "large": 1.2, "xlarge": 1.3}  # static

    def __init__(self, sid=0, sname="", type="", price=0.0, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.base_price = price
        self.size = size.lower()
        print("Shirt object created")

    def __del__(self):
        print(f"Shirt object for '{self.sname}' destroyed")

    def GetFinalPrice(self):
        factor = Shirt.size_factor.get(self.size, 1.0)
        return self.base_price * factor

    def ShowBook(self):
        print("----- Shirt Details -----")
        print("Shirt ID   :", self.sid)
        print("Shirt Name :", self.sname)
        print("Type       :", self.type)
        print("Size       :", self.size)
        print("Price      :", self.GetFinalPrice())


for sz in ["small", "medium", "large", "xlarge"]:
    s = Shirt(301, "Formal Shirt", "Formal", 1000.0, sz)
    s.ShowBook()