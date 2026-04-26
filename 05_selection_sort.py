def selection_sort(arr):
    for i in range(len(arr)):
        m = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[m] = arr[m], arr[i]
    return arr

print(selection_sort([64, 25, 12, 22, 11]))
