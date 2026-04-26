def binary_search(arr, x):
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] == x: return m
        elif arr[m] < x: l = m+1
        else: r = m-1
    return -1

arr = [10, 20, 30, 40, 50]
print(f"Found at index: {binary_search(arr, 30)}")
