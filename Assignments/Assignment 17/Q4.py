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


class College:
    def __init__(self, num_students=0):
        self.num_students = num_students
        self.students = []

    def AddStudent(self, student):
        self.students.append(student)
        self.num_students = len(self.students)
        print(f"Student '{student.Name}' added successfully.")

    def GetStudent(self, student_id):
        for s in self.students:
            if s.StudentId == student_id:
                return s
        print("Student not found.")
        return None

    def RemoveStudent(self, student_id):
        for s in self.students:
            if s.StudentId == student_id:
                self.students.remove(s)
                self.num_students = len(self.students)
                print(f"Student with ID {student_id} removed.")
                return
        print("Student not found.")

    def __str__(self):
        result = f"College has {self.num_students} student(s):\n"
        for s in self.students:
            result += str(s) + "\n"
        return result


# ---- Demo ----
college = College()

e1 = EnggStudent(101, "Rahul", 20, 85.5, "Computer Engineering", 40)
m1 = MedicalStudent(102, "Sneha", 21, 88.0, "Cardiology", 45)

college.AddStudent(e1)
college.AddStudent(m1)

print(college)

print("--- Get Student 101 ---")
print(college.GetStudent(101))

print("--- Remove Student 102 ---")
college.RemoveStudent(102)
print(college)