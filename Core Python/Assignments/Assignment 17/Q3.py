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


class MedicalStudent(Student):
    def __init__(self, student_id, name, age, percentage, specialization, marks_of_internship):
        super().__init__(student_id, name, age, percentage)
        self.Specialization = specialization
        self.MarksOfInternship = marks_of_internship

    def Accept(self):
        super().Accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Marks of Internship: "))

    def Display(self):
        super().Display()
        print(f"Specialization    : {self.Specialization}")
        print(f"MarksOfInternship : {self.MarksOfInternship}")

    def CalculateRank(self):
        total = (self.Percentage + self.MarksOfInternship) / 2
        if total >= 90:
            return "Rank A (Medical)"
        elif total >= 75:
            return "Rank B (Medical)"
        elif total >= 50:
            return "Rank C (Medical)"
        else:
            return "Rank D (Medical)"

    def __str__(self):
        return f"[MedicalStudent] {self.Name}, Specialization: {self.Specialization}, Internship Marks: {self.MarksOfInternship}"


# ---- Demo ----
m1 = MedicalStudent(102, "Sneha", 21, 88.0, "Cardiology", 45)
m1.Display()
print("Rank:", m1.CalculateRank())
print(m1)