//create a two pointer example in java with descriptive comments

int[] array = {1, 2, 3, 4, 5};
int left = 0;
int right = array.length - 1;

while (left < right) {
    // swap elements at left and right indices
    int temp = array[left];
    array[left] = array[right];
    array[right] = temp;

    // move pointers towards the middle of the array
    left++;
    right--;