def linear_search(arr, x):
    for i, v in enumerate(arr):
        if v == x: return i
    return -1

arr = [10, 20, 30, 40, 50]
x = 30
print(f"Found at index: {linear_search(arr, x)}")
