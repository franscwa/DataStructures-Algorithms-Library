#implement binary search in python with descriptive comments

def binary_search(arr, target):
    """
    Given a sorted array of integers and a target value, 
    return the index of the target value if found, 
    else return -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        # find the middle element of the array
        mid = (left + right) // 2

        # if the target is the middle element, return the index
        if arr[mid] == target:
            return mid

        # if the target is less than the middle element, 
        # search the left side of the array
        elif target < arr[mid]:
            right = mid - 1

        # if the target is greater than the middle element, 
        # search the right side of the array
        else:
            left = mid + 1

    # if the target is not found in the array, return -1
    return -1