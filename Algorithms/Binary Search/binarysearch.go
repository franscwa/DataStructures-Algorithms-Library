package main
func binarySearch(nums []int, target int) int {
	// set left and right pointers
	left := 0
	right := len(nums) - 1

	// run binary search until left pointer is less than right pointer
	for left <= right {
		// calculate middle index
		mid := left + (right-left)/2

		// if target is found at middle index, return index
		if nums[mid] == target {
			return mid
		}

		// if target is less than element at middle index,
		// search left side of array
		if target < nums[mid] {
			right = mid - 1
		}

		// if target is greater than element at middle index,
		// search right side of array
		if target > nums[mid] {
			left = mid + 1
		}
	}

	// if target is not found, return -1
	return -1
}