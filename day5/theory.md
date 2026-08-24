📦 Part 1: 
Strategic Concepts for Array Manipulation
When solving array (list) problems in interviews or assignments, you will typically rely on three foundational strategies:

1. **Linear Scans (\(O(n)\))**: Single passes through the array to check or accumulate values (e.g., finding the min/max or sum).
2. **Hash Maps / Sets (\(O(n)\) Space)**: Storing elements in a set or dict to instantly remember what you have already seen. This avoids slow nested loops.
3. **Two-Pointer Technique (\(O(1)\) Space)**: Placing tracking markers at different index positions (like the start and end) and moving them toward each other to modify the list in place without using extra memory.