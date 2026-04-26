list=[10,12,13,54,23,44,66,5,33,42]
n=len(list)
for i in range (n):
    min=i
    for j in range (i+1,n):
        if list[j]<list[min]:
            min=j
    list[i], list[min] = list[min], list[i]
print(list)


