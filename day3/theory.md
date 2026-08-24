### 1. Functions
    - Functions are reusable blocks of code designed to perform a specific task.


```python 
def greet_student(name, greeting="Hello"):  # 'name' is a parameter, 'greeting' has a default argument
    return f"{greeting}, {name}!"           # 'return' sends data back

```
**Key Terms :**
- Parameters:
     Variables listed in the function definition (e.g., name, greeting).
- Arguments: 
    Actual values passed to the function when calling it (e.g., greet_student("Alice")).
- Return:
     Exits a function and passes a value back to the caller. If omitted, it returns None.
- Default Arguments:
 Parameters that take a default value if no argument is provided (e.g., greeting="Hello").
 - Keyword Arguments: Passing arguments by explicitly naming the parameter during the function call (e.g., greet_student(name="Bob", greeting="Hi")).
 - Scope: Where a variable is visible. Local variables inside a function cannot be accessed outside it. Global variables are accessible everywhere.
 - Recursion: A function that calls itself to break down complex problems (like the list flattener we analyzed earlier).

- *args: Allows a function to accept any number of positional arguments as a tuple.
- **kwargs: Allows a function to accept any number of keyword arguments as a dictionary.
- Lambda: Anonymous, single-line functions used for quick, simple operations
```python
square = lambda x: x * x
print(square(5))  # Output: 25

```

###  Exception Handling
* Exception handling prevents your program from crashing when an error occurs.

*Key terms:*
- try : Houses the code that might trigger an error 
- except :  Captures and handles specific errors if they happens inside try block 
- finally: Executes code cleanup (like closing a file) regardless of whether an error occurred or not.
- raise: Manually triggers an exception when a specific condition is violated.



## File Handling and JSON ::
- File operations allow your program to save data permanently on your hard drive . 

**with**:
automatically closes the file when done , even if error occures .

with open('data.txt', 'r') as file:
data =  file.read();


File Modes
- r (Read): Opens a file for reading. Raises an error if the file does not exist. 
- w (Write): Opens a file for writing. Overwrites existing content or creates a new file.
- a (Append): Opens a file for adding data to the end without deleting existing content.

JSON (JavaScript Object Notation)JSON is a lightweight data format used to save structural data (like Python dictionaries) into text files.
json.dumps(obj): Converts a Python object (dictionary/list) into a JSON string (Data to String).
json.loads(string): Converts a JSON string back into a Python object (String to Data).
