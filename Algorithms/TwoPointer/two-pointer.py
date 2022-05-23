def twoPointers(arr, target): 
      
    n = len(arr) 
    ptr1, ptr2 = 0, 1
  
    while ptr1 < n and ptr2 < n: 
        if ptr1 != ptr2 and arr[ptr1] + arr[ptr2] == target: 
            return ptr1, ptr2 
        elif ptr1 != ptr2 and arr[ptr1] + arr[ptr2] < target: 
            ptr2 += 1
        else: 
            ptr1 += 1
            
    return -1