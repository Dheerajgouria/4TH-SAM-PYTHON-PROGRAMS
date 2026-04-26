# ============================================
# Practical 28: File Handling in Python
# ============================================
# Aim: Demonstrate reading, writing, and appending to files

filename = "student_data.txt"

# ---- Writing to a file ----
print("--- Writing to File ---")
with open(filename, "w") as f:
    f.write("Name: Dheeraj Gouria\n")
    f.write("Roll No: 21\n")
    f.write("Branch: Computer Science\n")
    f.write("Marks: 85\n")
print(f"Data written to '{filename}' successfully.\n")

# ---- Reading from a file ----
print("--- Reading from File ---")
with open(filename, "r") as f:
    content = f.read()
    print(content)

# ---- Appending to a file ----
print("--- Appending to File ---")
with open(filename, "a") as f:
    f.write("Grade: A\n")
print("Data appended successfully.\n")

# ---- Reading line by line ----
print("--- Reading Line by Line ---")
with open(filename, "r") as f:
    for line_no, line in enumerate(f, start=1):
        print(f"Line {line_no}: {line.strip()}")

# ---- Count lines and words ----
with open(filename, "r") as f:
    lines = f.readlines()

print(f"\nTotal Lines : {len(lines)}")
print(f"Total Words : {sum(len(l.split()) for l in lines)}")

# Output Example:
# Data written to 'student_data.txt' successfully.
# Name: Dheeraj Gouria
# Roll No: 21
