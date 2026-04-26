# ============================================
# Practical 26: Dictionary Operations
# ============================================
# Aim: Perform various dictionary operations in Python

# Creating a student dictionary
student = {
    "name"    : "Dheeraj",
    "roll_no" : 21,
    "branch"  : "Computer Science",
    "marks"   : 85
}

print("--- Dictionary Operations ---")
print(f"Student Record : {student}")
print(f"Name           : {student['name']}")
print(f"Roll No        : {student['roll_no']}")

# Adding a new key
student["grade"] = "A"
print(f"After adding grade: {student}")

# Updating a value
student["marks"] = 90
print(f"Updated Marks  : {student['marks']}")

# Deleting a key
del student["roll_no"]
print(f"After deleting roll_no: {student}")

# Iterating over dictionary
print("\nAll Keys and Values:")
for key, value in student.items():
    print(f"  {key} : {value}")

# Checking if key exists
print(f"\n'name' in student : {'name' in student}")
print(f"Total keys        : {len(student)}")

# Output Example:
# Student Record : {'name': 'Dheeraj', 'roll_no': 21, ...}
# Name           : Dheeraj
