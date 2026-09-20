from abc import ABC, abstractmethod

class Emp(ABC):
    def __init__(self, id, name, sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getName(self):
        return self.name

    def setName(self, newId):
        self.name = newId

    def getSal(self):
        return self.sal

    def setSal(self, newId):
        self.sal = newId

    @abstractmethod
    def casal(self):
        pass

    def __str__(self):
        return f"ID={self.id}\t Name={self.name}\t Sal={self.sal}"
# Class EMp Ends

class Hr(Emp):
    def __init__(self, id, name, sal, com):
        super().__init__(id, name, sal)
        self.com = com

    def getCom(self):
        return self.com

    def setCom(self, com):
        self.com = com

    def casal(self):
        return self.com + self.sal

    def __str__(self):
        return super().__str__() + f"\tcom={self.com}"
# HrEnds Here

class Dev(Emp):
    def __init__(self, id, name, sal, bon):
        super().__init__(id, name, sal)
        self.bonus = bon

    def getBonus(self):
        return self.bonus

    def setBonus(self, bonus):
        self.bonus = bonus

    def casal(self):
        return self.bonus + self.sal

    def __str__(self):
        return super().__str__() + f"\tBonus={self.bonus}"

#*******************************************************
e1 = Emp(12, "Jgdish", 232323)
h1 = Hr(18, "Smriti", 333333, 1212)
d1 = Dev(1, "Rahul", 3434343, 2212)
print(e1.casal())
print(h1.casal())
print(h1)
print(d1)