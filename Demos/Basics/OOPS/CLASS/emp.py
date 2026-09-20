class Emp:
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal

    def getId(self):
        return self.id
    def setId(self,newId):
        self.id = newId

    def getName(self):
        return self.name
    def setName(self,newName):
        self.name = newName

    def getSal(self):
        return self.sal
    def setSal(self,newSal):
        self.sal = newSal

    def display(self):
         print("ID = {self.id} Name = {self.name} Salary = {self.sal}")

e1 = Emp(101, "Saee", 60000)
e2 = Emp(102, "aryan", 300000)
print(e1.getSal())
e1.setSal(2308999)
print(e1.getSal()) 
    





    
        