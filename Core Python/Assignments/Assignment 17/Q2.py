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


class EnggStudent(Student):
    def __init__(self, student_id, name, age, percentage, branch, internal_marks):
        super().__init__(student_id, name, age, percentage)
        self.Branch = branch
        self.InternalMarks = internal_marks

    def Accept(self):
        super().Accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    def Display(self):
        super().Display()
        print(f"Branch        : {self.Branch}")
        print(f"InternalMarks : {self.InternalMarks}")

    def CalculateRank(self):
        total = (self.Percentage + self.InternalMarks) / 2
        if total >= 90:
            return "Rank A (Engineering)"
        elif total >= 75:
            return "Rank B (Engineering)"
        elif total >= 50:
            return "Rank C (Engineering)"
        else:
            return "Rank D (Engineering)"

    def __str__(self):
        return f"[EnggStudent] {self.Name}, Branch: {self.Branch}, Internal Marks: {self.InternalMarks}"


# ---- Demo ----
e1 = EnggStudent(101, "Rahul", 20, 85.5, "Computer Engineering", 40)
e1.Display()
print("Rank:", e1.CalculateRank())
print(e1)