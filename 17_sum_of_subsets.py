def sum_of_subsets(arr, target, i=0, curr=[]):
    if sum(curr) == target: print(curr); return
    for j in range(i, len(arr)):
        if sum(curr)+arr[j] <= target:
            sum_of_subsets(arr, target, j+1, curr+[arr[j]])

sum_of_subsets([1,2,3,4,5], 5)
