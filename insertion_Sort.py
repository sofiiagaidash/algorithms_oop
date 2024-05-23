def bubble_sort(lst):
    for n in range(len(lst)):
        for i in range(n+1,len(lst)):
            if lst[n] < lst[i]:
                lst[n],lst[i] = lst[i],lst[n]
    return lst
print(bubble_sort([3,1,4,5,6,2,7,8]))