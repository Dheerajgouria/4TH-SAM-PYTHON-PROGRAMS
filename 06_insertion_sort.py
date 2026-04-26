def insertion_sort(arr):
    for i in range(1, len(arr)):
        k, j = arr[i], i-1
        while j >= 0 and arr[j] > k:
            arr[j+1] = arr[j]; j -= 1
        arr[j+1] = k
    return arr

print(insertion_sort([12, 11, 13, 5, 6]))
