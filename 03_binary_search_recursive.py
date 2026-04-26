def binary_search(arr, x, l=0, r=None):
    if r is None: r = len(arr)-1
    if l > r: return -1
    m = (l+r)//2
    if arr[m] == x: return m
    elif arr[m] < x: return binary_search(arr, x, m+1, r)
    else: return binary_search(arr, x, l, m-1)

arr = [10, 20, 30, 40, 50]
print(f"Found at index: {binary_search(arr, 30)}")
