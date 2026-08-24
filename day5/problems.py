def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    # Keep swapping until pointers meet in the middle
    while left < right:
        # Python shortcut to swap two variables without a temporary variable
        arr[left], arr[right] = arr[right], arr[left]
        
        # Move pointers closer together
        left += 1
        right -= 1
        
    return arr



def find_missing_number(arr, n):
    # Using integer division (//) to avoid converting into a float
    expected_sum = (n * (n + 1)) // 2
    
    # Add up all numbers currently present in the list
    actual_sum = sum(arr)
    
    # The difference is your answer
    return expected_sum - actual_sum

