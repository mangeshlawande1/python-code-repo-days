name = "  Python Programming  "

# # 1. Indexing & Slicing
# print(name[2])          # 'P' (Zero-indexed)
# print(name[2:8])        # 'Python' (Slicing [start:stop])


# # 2. Case Modifications
# print(name.upper())     # "  PYTHON PROGRAMMING  "
# print(name.lower())     # "  python programming  "~


#3. Clean up and modification 
# print(name.strip())     # "Python Programming" (Removes leading/trailing whitespace)
# print(name.replace("Python", "Java")) # "  Java Programming  "

## 4 split and join a string
# words = name.split()    # ['Python', 'Programming'] (Splits by space by default)
# print("-".join(words))  # "Python-Programming" (Combines elements with a delimiter)

# # 5. Finding Substrings
# print(name.find("Pro")) # 9 (Returns starting index, or -1 if not found)




'''
Lists

'''

# numbers = [10, 20, 30, 40]

# # 1. Adding Elements
# numbers.append(50)       # [10, 20, 30, 40, 50] (Adds to the end)
# numbers.insert(1, 15)    # [10, 15, 20, 30, 40, 50] (Inserts 15 at index 1)

# # 2. Removing Elements
# numbers.remove(20)       # [10, 15, 30, 40, 50] (Removes first occurrence of value 20)
# popped = numbers.pop()   # Removes and returns last element (50). List is now [10, 15, 30, 40]



# 3. Reordering
# numbers.sort()           # Sorts the list in ascending order in-place
# numbers.reverse()        # Reverses the list elements in-place


# 4. Slicing
# print(numbers[1:3])      # Returns a sublist from index 1 to 2


### Tuple 

# data = (10, 20, 30)
# data[0] = 99 <-- This will raise a TypeError


### Sets: 
# numbers_set = {1, 2, 3, 3} 
# print(numbers_set) # Output: {1, 2, 3} (Duplicates are automatically removed)


# student = {
#     "name": "Mangesh",
#     "age": 22
# }

# 1. Accessing Data Safely
# print(student.get("name"))       # "Mangesh"
# print(student.get("grade", "N/A")) # "N/A" (Returns default instead of throwing KeyError)

# # 2. Extracting Components
# print(student.keys())    # dict_keys(['name', 'age'])
# print(student.values())  # dict_values(['Mangesh', 22])
# print(student.items())   # dict_items([('name', 'Mangesh'), ('age', 22)])

# # 3. Updating and Deleting
# student["age"] = 23      # Updates existing key
# student["city"] = "Pune" # Adds new key-value pair
# del student["city"]      # Deletes the key "city"

# text = "fresher challenge"
# t1 ="python programming"
# vowels = "aeiouAEIOU"
# count = sum(1 for char in t1 if char in vowels)
# print("Vowels count:", count)

# text = "hello"
# print("Length:", len(text))

# text = "programming"
# seen = set()
# duplicates = set()
# for char in text:
#     if char in seen:
#         duplicates.add(char)
#     else:
#         seen.add(char)
# print("Duplicates:", list(duplicates))
# print("Unique characters:", list(seen - duplicates))
# print(duplicates)  # Output: {'g', 'r', 'm'}


# nums = [5, 2, 9, 1]
# for i in range(len(nums)):
#     for j in range(0, len(nums) - i - 1):
#         if nums[j] > nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print("Sorted:", nums)



## merged dict 
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# Method 1 (Python 3.5+):

# merged = {**dict1, **dict2} 
# Note: duplicate keys get overridden by the second dict
# print("Merged:", merged)


## find freq of elements
# items = ['apple', 'banana', 'apple']
# freq = {}; 
# for item in items:
#     freq[item] = freq.get(item, 0) + 1
# print("Frequency:", freq)  # Output: {'apple': 2, 'banana': 1}


# Input
# text = "programming"

# # Frequency counter map
# frequency = {}

# # Process each character
# for char in text:
#     frequency[char] = frequency.get(char, 0) + 1

# # Output in requested format
# for key, value in frequency.items():
#     print(f"{key} = {value}")

# # print("Frequency Map:", frequency)  # Output: {'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 1, 'n': 1}





def is_anagram(str1, str2):
    # Clean whitespace and force lowercase
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()
    
    # Quick optimization check
    if len(s1) != len(s2):
        return False
        
    # Count frequencies
    count = {}
    for char in s1:
        count[char] = count.get(char, 0) + 1
        
    # Subtract frequencies
    for char in s2:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
            
    return True

# # Example Walkthrough
# print("Is 'listen' and 'silent' an anagram?", is_anagram("listen", "silent")) 
# # Output: True

def find_second_largest(numbers):
# ensure 2 elements are present in list     
    if len(numbers) < 2:
        return None
        
    largest = float('-inf')
    second_largest = float('-inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
            
    return second_largest if second_largest != float('-inf') else None

# Example Walkthrough
sample_list = [12, 35, 1, 10, 34, 1]
print("Second largest element:", find_second_largest(sample_list))
# Output: 34


## list flattening 
# def flatten_list(nested_l):
#     flat_list = []
#     for item in nested_l:
#         if isinstance(item, list):
#             flat_list.extend(flatten_list(item))  # Recursively flatten
#         else:
#             flat_list.append(item)
#     return flat_list



# # Example Walkthrough
# nested_list = [1, [2, [3, 4], 5], 6]
# print("Flattened list:", flatten_list(nested_list))

def flatten_list(nested_list):
    # Reads as: take item for each sublist, then take element out of each sublist
    return [element for sublist in nested_list for element in sublist]

# Example Walkthrough
matrix = [[1, 2], [3, 4]]
print("Flattened list:", flatten_list(matrix))
# Output: [1, 2, 3, 4]
