def selection_sort(arr):
    for x in range(len(arr)):
        minimum = x
        for y in range(x+1,len(arr)):
            if arr[minimum] > arr[y]:
                minimum = y
            arr[minimum],arr[x] = arr[x],arr[minimum]
    return arr
print(selection_sort([2,3,4,1,5,7,6,8]))
