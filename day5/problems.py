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

def find_multiple_missing(arr, n):
    # 1. Convert the list to a set for instant O(1) lookups
    present_numbers = set(arr)
    missing_numbers = []
    
    # 2. Check every number that should be there
    for i in range(1, n + 1):
        # 3. If it's missing, catch it
        if i not in present_numbers:
            missing_numbers.append(i)
            
    return missing_numbers

# Verification
# Range is 1 to 7. Numbers 3 and 6 are missing.
sample_arr = [2, 5, 1, 7, 4] 
print(find_multiple_missing(sample_arr, 7)) # Output: [3, 6]
