# Quick Sort Implementation:

#import random # For the testing portion

# Altered for metadata
def quick_sort(arr, key=lambda x: x):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if key(x) < key(pivot)]
    middle = [x for x in arr if key(x) == key(pivot)]
    right = [x for x in arr if key(x) > key(pivot)]

    return quick_sort(left, key) + middle + quick_sort(right, key)

# Testing the Algorithm
#random_list = [random.randint(10, 9999) for _ in range(10)]


#print("Original Array: ", random_list)
#sorted_arr = quick_sort(random_list)
#print("Sorted Array: ", sorted_arr)
