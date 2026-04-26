# ============================================
# Practical 23: Armstrong Number
# ============================================
# Aim: Write a program to check if a number is an Armstrong number
# Armstrong number: sum of digits each raised to power of number of digits
# Example: 153 = 1^3 + 5^3 + 3^3 = 153

num = int(input("Enter a number: "))

digits = str(num)
power = len(digits)

total = sum(int(d) ** power for d in digits)

if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is NOT an Armstrong number.")

# Output Example 1:
# Enter a number: 153
# 153 is an Armstrong number.

# Output Example 2:
# Enter a number: 123
# 123 is NOT an Armstrong number.
