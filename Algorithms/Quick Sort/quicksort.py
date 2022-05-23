#implement quick sort in python with descriptive comments

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Quicksort is a divide and conquer algorithm. It works by partitioning an array into two smaller arrays, 
# one containing elements less than the pivot element and one containing elements greater than the pivot element. 
# The algorithm then recursively sorts the two smaller arrays.