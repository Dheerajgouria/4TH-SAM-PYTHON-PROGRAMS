# ============================================
# Practical 25: List Operations
# ============================================
# Aim: Perform various list operations in Python

# Creating a list
my_list = []
n = int(input("How many elements to enter: "))

for i in range(n):
    elem = int(input(f"Enter element {i+1}: "))
    my_list.append(elem)

print("\n--- List Operations ---")
print(f"Original List : {my_list}")
print(f"Sorted List   : {sorted(my_list)}")
print(f"Reversed List : {my_list[::-1]}")
print(f"Maximum       : {max(my_list)}")
print(f"Minimum       : {min(my_list)}")
print(f"Sum           : {sum(my_list)}")
print(f"Length        : {len(my_list)}")

# Removing duplicate elements
unique = list(set(my_list))
print(f"Unique Elements: {unique}")

# List slicing
print(f"First 3 elements: {my_list[:3]}")
print(f"Last 3 elements : {my_list[-3:]}")

# Output Example:
# Original List : [5, 3, 8, 1, 9]
# Sorted List   : [1, 3, 5, 8, 9]
# Maximum       : 9
# Minimum       : 1
