# ============================================
# Practical 24: String Operations
# ============================================
# Aim: Perform various string operations in Python

s = input("Enter a string: ")

print("\n--- String Operations ---")
print(f"Original String      : {s}")
print(f"Uppercase            : {s.upper()}")
print(f"Lowercase            : {s.lower()}")
print(f"Length               : {len(s)}")
print(f"Reversed             : {s[::-1]}")
print(f"Is Palindrome        : {s == s[::-1]}")
print(f"Title Case           : {s.title()}")
print(f"Replace spaces with _: {s.replace(' ', '_')}")
print(f"Count vowels         : {sum(1 for c in s.lower() if c in 'aeiou')}")
print(f"Strip whitespace     : '{s.strip()}'")

# Output Example:
# Enter a string: hello world
# Uppercase            : HELLO WORLD
# Lowercase            : hello world
# Length               : 11
# Reversed             : dlrow olleh
# Is Palindrome        : False
