# ============================================
# Practical 29: Exception Handling in Python
# ============================================
# Aim: Demonstrate try, except, else, finally blocks

# ---- Example 1: Division by Zero ----
print("--- Division Example ---")
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter valid integers!")
else:
    print(f"Result: {a} / {b} = {result:.2f}")
finally:
    print("Division operation completed.\n")

# ---- Example 2: List Index Error ----
print("--- List Index Example ---")
my_list = [10, 20, 30, 40, 50]
try:
    index = int(input(f"Enter index (list has {len(my_list)} elements): "))
    print(f"Element at index {index}: {my_list[index]}")
except IndexError:
    print("Error: Index out of range!")
except ValueError:
    print("Error: Please enter a valid integer index!")
finally:
    print("List access operation completed.\n")

# ---- Example 3: File Not Found ----
print("--- File Reading Example ---")
try:
    with open("nonexistent_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("File operation completed.")

# Output Example:
# Enter numerator: 10
# Enter denominator: 0
# Error: Cannot divide by zero!
# Division operation completed.
