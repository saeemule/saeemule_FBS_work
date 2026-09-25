import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from symarks import SYMARKS
from tymarks import TYMarks



class Student:
    def __init__(self, roll_number, name, sy_marks, ty_marks):
        self.RollNumber = roll_number
        self.Name = name
        self.SYMarks = sy_marks   # object of SYMARKS
        self.TYMarks = ty_marks   # object of TYMarks

    def CalculateGrade(self):
        # Add SY Computer marks + TY (Theory + Practical)
        total_computer_marks = self.SYMarks.ComputerTotal + self.TYMarks.Theory + self.TYMarks.Practical

        # Assuming SY Computer out of 100 and TY out of 100 -> combined out of 200
        percentage = total_computer_marks / 2

        if percentage >= 70:
            return "A", percentage
        elif percentage >= 60:
            return "B", percentage
        elif percentage >= 50:
            return "C", percentage
        elif percentage >= 40:
            return "Pass Class", percentage
        else:
            return "Fail", percentage

    def Display(self):
        grade, percentage = self.CalculateGrade()
        print("=" * 45)
        print(f"Roll Number : {self.RollNumber}")
        print(f"Name        : {self.Name}")
        print(self.SYMarks)
        print(self.TYMarks)
        print(f"Total Computer Marks (SY+TY) : {self.SYMarks.ComputerTotal + self.TYMarks.Theory + self.TYMarks.Practical}")
        print(f"Percentage  : {percentage:.2f}%")
        print(f"Grade       : {grade}")
        print("=" * 45)


# ---- Demo ----
if __name__ == "__main__":
    sy_marks = SYMARKS(computer_total=75, maths_total=68, electronics_total=72)
    ty_marks = TYMarks(theory=65, practical=28)

    student1 = Student(roll_number=101, name="Rohan Sharma", sy_marks=sy_marks, ty_marks=ty_marks)
    student1.Display()