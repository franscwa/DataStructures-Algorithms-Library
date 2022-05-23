#write a python program with a two pointer example with descriptive comments

# this is an example of a two pointer algorithm

def two_sum(nums, target):
    # create two pointers, one at the beginning of the list
    # and one at the end
    i = 0
    j = len(nums) - 1

    # loop until the two pointers meet in the middle
    while i < j:
        # if the sum of the two numbers at the pointers is equal to the target
        # then we have found a match and can return the indices
        if nums[i] + nums[j] == target:
            return [i, j]
        # if the sum is less than the target, then we need to increase the
        # value of the left pointer so that we can get closer to the target
        elif nums[i] + nums[j] < target:
            i += 1
        # if the sum is greater than the target, then we need to decrease the
        # value of the right pointer so that we can get closer to the target
        else:
            j -= 1

    # if we reach this point, then it means that we did not find a match
    return [-1, -1]