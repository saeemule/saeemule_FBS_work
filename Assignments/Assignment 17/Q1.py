class Student:
    def __init__(self, student_id, name, age, percentage):
        self.StudentId = student_id
        self.Name = name
        self.Age = age
        self.Percentage = percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def Display(self):
        print(f"Student ID : {self.StudentId}")
        print(f"Name       : {self.Name}")
        print(f"Age        : {self.Age}")
        print(f"Percentage : {self.Percentage}")

    def CalculateRank(self):
        if self.Percentage >= 90:
            return "Rank A"
        elif self.Percentage >= 75:
            return "Rank B"
        elif self.Percentage >= 50:
            return "Rank C"
        else:
            return "Rank D"

    def __str__(self):
        return f"[Student] {self.Name} (ID: {self.StudentId}), Age: {self.Age}, %: {self.Percentage}"


# ---- Demo ----
s1 = Student(1, "Amit", 19, 78.5)
s1.Display()
print("Rank:", s1.CalculateRank())
print(s1)