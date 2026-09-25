class Emp:
    def __init__(self, eid, ename, basic):
        self.eid = eid
        self.ename = ename
        self.basic = basic

    def __str__(self):
        return f"ID: {self.eid}, Name: {self.ename}, Basic: {self.basic}"


# ---- Demo ----
e1 = Emp(101, "Rahul", 25000)
print(e1)