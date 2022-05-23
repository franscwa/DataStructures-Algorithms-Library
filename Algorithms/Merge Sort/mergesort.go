//implement merge sort in go with descriptive comments

package main

func mergeSort(arr []int) []int {
	if len(arr) <= 1 { //if the length of the array is 1 or 0, then it is already sorted
		return arr
	}

	mid := len(arr) / 2 //find the middle index of the array
	left := arr[:mid]    //create a slice of the left side of the array
	right := arr[mid:]   //create a slice of the right side of the array

	return merge(
		mergeSort(left),   //recursively call mergeSort on the left side
		mergeSort(right),  //recursively call mergeSort on the right side
	)
}

func merge(left, right []int) []int {
	results := []int{} //create an empty array to store our results

	for len(left) > 0 && len(right) > 0 { //while there are still elements in both slices
		if left[0] < right[0] { //if the first element in the left slice is less than the first element in the right slice
			results = append(results, left[0]) //append the first element in the left slice to the results
			left = left[1:]                    //remove the first element from the left slice
		} else { //if the first element in the right slice is less than or equal to the first element in the left slice
			results = append(results, right[0]) //append the first element in the right slice to the results
			right = right[1:]                   //remove the first element from the right slice
		}
	}

	//if there are still elements in the left slice, append them all to the results
	for i := 0; i < len(left); i++ {
		results = append(results, left[i])
	}

	//if there are still elements in the right slice, append them all to the results
	for i := 0; i < len(right); i++ {
		results = append(results, right[i])
	}

	return results //return the sorted array
}