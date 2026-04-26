# ============================================
# Practical 27: Functions - Default & Keyword Arguments
# ============================================
# Aim: Demonstrate use of functions with default and keyword arguments

# ---- Simple Function ----
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Dheeraj")                    # uses default message
greet("Rahul", "Good Morning")      # custom message
greet(message="Hey", name="Priya")  # keyword arguments

print()

# ---- Function to calculate Simple Interest ----
def simple_interest(principal, rate=5, time=1):
    si = (principal * rate * time) / 100
    return si

print("Simple Interest Examples:")
print(f"SI (default rate & time) : {simple_interest(1000)}")
print(f"SI (custom rate)         : {simple_interest(1000, rate=8)}")
print(f"SI (all custom)          : {simple_interest(5000, rate=10, time=3)}")

print()

# ---- Function with *args (variable arguments) ----
def add_all(*numbers):
    return sum(numbers)

print(f"Sum of 1,2,3     : {add_all(1, 2, 3)}")
print(f"Sum of 1,2,3,4,5 : {add_all(1, 2, 3, 4, 5)}")

# Output Example:
# Hello, Dheeraj!
# Good Morning, Rahul!
# SI (default rate & time) : 50.0
