# ============================================
# Practical 30: Classes and Objects (OOP)
# ============================================
# Aim: Demonstrate Object Oriented Programming in Python
#      using classes, objects, constructors, and methods

class Student:
    # Class variable
    college = "Government Degree College"

    # Constructor
    def __init__(self, name, roll_no, marks):
        self.name    = name
        self.roll_no = roll_no
        self.marks   = marks

    # Method to display student info
    def display(self):
        print(f"\n--- Student Details ---")
        print(f"College  : {Student.college}")
        print(f"Name     : {self.name}")
        print(f"Roll No  : {self.roll_no}")
        print(f"Marks    : {self.marks}")
        print(f"Grade    : {self.get_grade()}")

    # Method to calculate grade
    def get_grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F (Fail)"

    # Method to check pass/fail
    def result(self):
        if self.marks >= 40:
            print(f"{self.name} has PASSED.")
        else:
            print(f"{self.name} has FAILED.")


# ---- Creating Objects ----
s1 = Student("Dheeraj Gouria", 21, 88)
s2 = Student("Rahul Sharma",   15, 72)
s3 = Student("Priya Kumari",   30, 55)

# ---- Displaying Details ----
s1.display()
s1.result()

s2.display()
s2.result()

s3.display()
s3.result()

# Output Example:
# --- Student Details ---
# College  : Government Degree College
# Name     : Dheeraj Gouria
# Roll No  : 21
# Marks    : 88
# Grade    : A
# Dheeraj Gouria has PASSED.
