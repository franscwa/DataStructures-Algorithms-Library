package main

import "crypto/rand"

func quicksort(a []int) []int {
	if len(a) < 2 {
		return a
	}

	left, right := 0, len(a)-1

	pivot := rand.Int() % len(a)

	a[pivot], a[right] = a[right], a[pivot]

	for i, _ := range a {
		if a[i] < a[right] {
			a[left], a[i] = a[i], a[left]
			left++
		}
	}

	a[left], a[right] = a[right], a[left]

	quicksort(a[:left])
	quicksort(a[left+1:])

	return a
}

// This function implements the quick sort algorithm in go.
// The quick sort algorithm works by taking an array of values and selecting a pivot value.
// The array is then partitioned such that all values less than the pivot are placed before it
// and all values greater than the pivot are placed after it.
// The array is then recursively sorted with the pivot in its correct position.
