def merge_sort(arr):
    # Base case - if the input array is only one element, return it
    if len(arr) == 1:
        return arr

    # Split the input array in half
    left = arr[:len(arr) // 2]
    right = arr[len(arr) // 2:]

    # Recursively call merge_sort on the left and right halves of the array
    left = merge_sort(left)
    right = merge_sort(right)

    # Initialize an empty array to store the merged array
    merged = []

    # While there are elements in both the left and right arrays:
    while len(left) > 0 and len(right) > 0:
        # If the first element in the left array is smaller than the first element in the right array:
        if left[0] < right[0]:
            # Append the first element in the left array to the merged array
            merged.append(left[0])
            # Remove the first element in the left array
            left = left[1:]
        # Otherwise:
        else:
            # Append the first element in the right array to the merged array
            merged.append(right[0])
            # Remove the first element in the right array
            right = right[1:]

    # If there are elements remaining in the left array:
    while len(left) > 0:
        # Append the first element in the left array to the merged array
        merged.append(left[0])
        # Remove the first element in the left array
        left = left[1:]

    # If there are elements remaining in the right array:
    while len(right) > 0:
        # Append the first element in the right array to the merged array
        merged.append(right[0])
        # Remove the first element in the right array
        right = right[1:]

    # Return the merged array
    return merged