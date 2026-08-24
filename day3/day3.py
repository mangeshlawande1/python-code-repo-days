# try: 
#     num = int(input("Enter a number: "))
#     result = 10 / num 
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")
# except ValueError:
#     print("Error: Not a valid Number.")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
# finally:
#     print("This code is always runs, no matter what.")
    


age = input("Enter your age: ")

try:
    age = int(age)
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Your age is: {age}")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("This code always runs, no matter what.")


## File Handling and json ::

with open('data.txt', 'r') as file:
    data =  file.read()



