
func KadanesAlgorithm(array []int) int {
	maxEndingHere := array[0]
	maxSoFar := array[0]
	for i := 1; i < len(array); i++ {
		num := array[i]
		maxEndingHere = max(num, maxEndingHere+num)
		maxSoFar = max(maxSoFar, maxEndingHere)
	}
	return maxSoFar
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}