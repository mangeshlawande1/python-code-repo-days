import collections

class ArrayDSA:
    
    @staticmethod
    def find_min_max(arr):
        """1 & 2. Find maximum and minimum in a single pass."""
        if not arr:
            return None, None
        
        maximum = float('-inf')
        minimum = float('inf')
        
        for num in arr:
            if num > maximum:
                maximum = num
            if num < minimum:
                minimum = num
        return maximum, minimum

    @staticmethod
    def find_second_largest(arr):
        """3. Find the second largest distinct number."""
        if len(arr) < 2:
            return None
        
        largest = float('-inf')
        second_largest = float('-inf')
        
        for num in arr:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num != largest:
                second_largest = num
                
        return second_largest if second_largest != float('-inf') else None

    @staticmethod
    def reverse_array(arr):
        """4. Reverse array in-place using Two-Pointers."""
        left = 0
        right = len(arr) - 1
        
        while left < right:
            # Swap values
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

    @staticmethod
    def remove_duplicates(arr):
        """5. Remove duplicates while maintaining order."""
        seen = set()
        unique_arr = []
        for num in arr:
            if num not in seen:
                seen.add(num)
                unique_arr.append(num)
        return unique_arr

    @staticmethod
    def find_duplicates(arr):
        """6. Find and isolate all duplicate elements."""
        seen = set()
        duplicates = set()
        for num in arr:
            if num in seen:
                duplicates.add(num)
            else:
                seen.add(num)
        return list(duplicates)

    @staticmethod
    def find_missing_number(arr, n):
        """7. Find the missing number in an consecutive range 1 to n."""
        # Arithmetic progression formula: Sum = n * (n + 1) / 2
        expected_sum = (n * (n + 1)) // 2
        actual_sum = sum(arr)
        return expected_sum - actual_sum

    @staticmethod
    def find_sum(arr):
        """8. Find total sum of the array."""
        total = 0
        for num in arr:
            total += num
        return total

    @staticmethod
    def count_frequency(arr):
        """9. Count occurrences of each element."""
        # Built-in equivalent to making a manual dictionary tracker loop
        return dict(collections.Counter(arr))

    @staticmethod
    def rotate_array(arr, k):
        """10. Rotate array to the right by k steps."""
        if not arr:
            return arr
        
        # Handle k values larger than the array length
        k = k % len(arr)
        
        # Slicing approach: Take the last k items and put them at the front
        return arr[-k:] + arr[:-k]


# ==========================================
# Execution Walkthrough & Verification
# ==========================================
if __name__ == "__main__":
    dsa = ArrayDSA()
    demo_list = [3, 5, 1, 5, 9, 2, 9, 8]
    
    print(f"Original List: {demo_list}\n")
    
    # 1 & 2. Max and Min
    mx, mn = dsa.find_min_max(demo_list)
    print(f"1 & 2. Max: {mx} | Min: {mn}")
    
    # 3. Second Largest
    print(f"3. Second Largest: {dsa.find_second_largest(demo_list)}")
    
    # 4. Reverse (Note: copy used to keep demo_list intact for next steps)
    print(f"4. Reversed List : {dsa.reverse_array(demo_list.copy())}")
    
    # 5. Remove Duplicates
    print(f"5. Without Duplicates: {dsa.remove_duplicates(demo_list)}")
    
    # 6. Find Duplicates
    print(f"6. Duplicates Found  : {dsa.find_duplicates(demo_list)}")
    
    # 7. Find Missing Number (Sequence 1 to 6 missing '4')
    sequence = [1, 2, 3, 5, 6]
    print(f"7. Missing Number from: {dsa.find_missing_number(sequence, 6)}")
    
    # 8. Find Sum
    print(f"8. Total Array Sum: {dsa.find_sum(demo_list)}")
    
    # 9. Frequency
    print(f"9. Frequencies: {dsa.count_frequency(demo_list)}")
    
    # 10. Rotate array by 3 steps
    print(f"10. Rotated by 3 steps: {dsa.rotate_array([1, 2, 3, 4, 5], 3)}")

