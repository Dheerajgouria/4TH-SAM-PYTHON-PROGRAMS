def radix_sort(arr):
    for exp in [10**i for i in range(len(str(max(arr))))]:
        buckets = [[] for _ in range(10)]
        for n in arr: buckets[(n//exp)%10].append(n)
        arr = [n for b in buckets for n in b]
    return arr

print(radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))
