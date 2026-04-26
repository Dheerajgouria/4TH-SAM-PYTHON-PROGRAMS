def merge_sort(arr):
    if len(arr) <= 1: return arr
    m = len(arr)//2
    l, r = merge_sort(arr[:m]), merge_sort(arr[m:])
    return [l.pop(0) if (r and l and l[0]<=r[0]) or not r else r.pop(0) for _ in range(len(l)+len(r))] + l + r

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
