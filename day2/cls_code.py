class StringHelper:
    """Handles core string operations and Day 2 interview puzzles."""
    def __init__(self, text):
        self.text = text

    def demonstrate_methods(self):
        """Displays transformations using built-in string methods."""
        print(f"Original: '{self.text}'")
        print(f"Upper:    '{self.text.upper()}'")
        print(f"Lower:    '{self.text.lower()}'")
        print(f"Stripped: '{self.text.strip()}'")
        print(f"Replaced: '{self.text.replace('Python', 'Code')}'")
        
        # Split & Join demonstration
        words = self.text.split()
        print(f"Split:    {words}")
        print(f"Joined:   {'-'.join(words)}")

    def reverse(self):
        return self.text[::-1]

    def is_palindrome(self):
        cleaned = "".join(self.text.split()).lower()
        return cleaned == cleaned[::-1]

    def count_vowels(self):
        vowels = "aeiouAEIOU"
        return sum(1 for char in self.text if char in vowels)

    def get_character_frequency(self):
        """Solves the Day 2 Challenge: Character counts."""
        frequency = {}
        for char in self.text:
            if char != " ":  # Exclude spaces for cleaner output
                frequency[char] = frequency.get(char, 0) + 1
        return frequency


class ListHelper:
    """Handles basic arrays, reordering, and element filtering."""
    def __init__(self, items):
        self.items = list(items)  # Creates a copy to protect original data

    def demonstrate_methods(self):
        """Modifies and reorders the list dynamically."""
        print(f"Original List:   {self.items}")
        
        self.items.append(99)
        print(f"After Append(99): {self.items}")
        
        self.items.insert(1, 55)
        print(f"After Insert(55): {self.items}")
        
        self.items.pop()
        print(f"After Pop (last): {self.items}")

    def remove_duplicates(self):
        return list(set(self.items))

    def get_min_max(self):
        return {"Min": min(self.items), "Max": max(self.items)}

    def manual_bubble_sort(self):
        """Sorts the array without using built-in methods."""
        arr = list(self.items)
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class TupleHelper:
    """Handles immutable sequence operations and data extraction."""
    def __init__(self, data_tuple):
        self.data = tuple(data_tuple)

    def demonstrate_immutability(self):
        """Shows standard read-only access and count methods."""
        print(f"Original Tuple:  {self.data}")
        print(f"Length of Tuple: {len(self.data)}")
        print(f"Element at idx 0:{self.data[0]}")
        
        # Interview concept: Tuples support count and index
        sample_element = self.data[0]
        print(f"Occurrences of {sample_element}: {self.data.count(sample_element)}")

    def unpack_elements(self):
        """Demonstrates standard variable unpacking."""
        if len(self.data) >= 3:
            a, b, c = self.data[:3]
            return f"Unpacked first 3 items: {a}, {b}, {c}"
        return "Tuple too short to unpack 3 items."

    def convert_to_list_and_modify(self, new_value):
        """Demonstrates the interview workaround to modify a tuple."""
        temp_list = list(self.data)
        temp_list.append(new_value)
        return tuple(temp_list)


class SetHelper:
    """Handles mathematical set logic, membership checks, and uniqueness."""
    def __init__(self, data_set):
        self.data = set(data_set)

    def demonstrate_methods(self):
        """Shows dynamic modifications of an unordered unique container."""
        print(f"Original Set:    {self.data} (Duplicates automatically dropped)")
        
        # Create a copy to show operations safely
        working_set = self.data.copy()
        working_set.add(99)
        print(f"After Add(99):   {working_set}")
        
        working_set.discard(99)  # Safer than remove() because it won't crash if 99 is missing
        print(f"After Discard(99):{working_set}")

    def perform_math_operations(self, other_collection):
        """Demonstrates core mathematical set operations popular in interviews."""
        other_set = set(other_collection)
        return {
            "Union": self.data.union(other_set),
            "Intersection": self.data.intersection(other_set),
            "Difference": self.data.difference(other_set)
        }


class DictionaryHelper:
    """Manages maps, extractions, and dataset combinations."""
    def __init__(self, primary_dict):
        self.data = primary_dict

    def demonstrate_views(self):
        """Prints dictionary structured parts cleanly."""
        print(f"Keys:   {list(self.data.keys())}")
        print(f"Values: {list(self.data.values())}")
        print(f"Items:  {list(self.data.items())}")

    def safe_lookup(self, key, default_value="Not Found"):
        return self.data.get(key, default_value)

    def merge_with(self, secondary_dict):
        """Combines two records using dictionary unpacking."""
        return {**self.data, **secondary_dict}


def main():
    print("=== 🧵 STRING WORKLIST ===")
    sample_text = "Python"
    str_tool = StringHelper(sample_text)
    str_tool.demonstrate_methods()
    print(f"Reversed:      {str_tool.reverse()}")
    print(f"Is Palindrome: {str_tool.is_palindrome()}")
    
    # Executing Day 2 Target Challenge
    print("\n--- Day 2 Target Challenge ('programming') ---")
    challenge_tool = StringHelper("programming")
    freq_map = challenge_tool.get_character_frequency()
    for char, count in freq_map.items():
        print(f"{char} = {count}")

    print("\n=== 📋 LIST WORKLIST ===")
    sample_list = [40, 10, 20, 30, 20]
    list_tool = ListHelper(sample_list)
    list_tool.demonstrate_methods()
    print(f"Unique Array:  {list_tool.remove_duplicates()}")
    print(f"Limits:        {list_tool.get_min_max()}")
    print(f"Bubble Sorted: {list_tool.manual_bubble_sort()}")

    print("\n=== 🔒 TUPLE WORKLIST ===")
    sample_tuple = (10, 20, 30, 10)
    tuple_tool = TupleHelper(sample_tuple)
    tuple_tool.demonstrate_immutability()
    print(tuple_tool.unpack_elements())
    print(f"Modified via list conversion: {tuple_tool.convert_to_list_and_modify(100)}")

    print("\n=== ⚡ SET WORKLIST ===")
    sample_set = {1, 2, 3, 3, 4}  # Notice the duplicate 3
    set_tool = SetHelper(sample_set)
    set_tool.demonstrate_methods()
    
    results = set_tool.perform_math_operations({3, 4, 5, 6})
    print(f"Union with {{3,4,5,6}}:        {results['Union']}")
    print(f"Intersection with {{3,4,5,6}}:  {results['Intersection']}")
    print(f"Difference (Self - Other):    {results['Difference']}")

    print("\n=== 📖 DICTIONARY WORKLIST ===")
    student_record = {"name": "Mangesh", "age": 22}
    dict_tool = DictionaryHelper(student_record)
    dict_tool.demonstrate_views()
    print(f"Safe Check:    {dict_tool.safe_lookup('grade', 'Pending')}")
    
    extra_details = {"city": "Pune", "age": 23}
    print(f"Merged Profile: {dict_tool.merge_with(extra_details)}")


if __name__ == "__main__":
    main()
