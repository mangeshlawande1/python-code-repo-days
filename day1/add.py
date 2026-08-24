# # Take input from the user and convert to floats
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# # Calculate the sum
# total = num1 + num2; 
# # Display the result
# print(f"The sum of {num1} and {num2} is {total}")

# num = int(input("Enter a number: ")); 

# if num % 2 == 0:
#     print(f"{num} is an even number.")
# else:
#     print(f"{num} is an odd number.")



# a = float(input("Enter first: "))
# b = float(input("Enter second: "))
# c = float(input("Enter third: "))

# largest = max(a, b, c)
# print(f"Largest is {largest}")


# # check positive or negative
# num = float(input("Enter a number: "))
# if num > 0:
#     print(f"{num} is a positive number.")
# elif num < 0:
#     print(f"{num} is a negative number.")
# else:
#     print(f"{num} is zero.")


# year = int(input("Enter a year: "));

# if(year %4 == 0 and year %100 !=0) or (year %400 ==0):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


# num = int(input("Enter table number: "))
# for i in range(1, 11):
#     print(f"{num} x {i} = {num * i}")


# what is factorial of a number 

# num  = int (input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
# print(f"The factorial of {num} is {factorial}.")

# check prime number 
num = int(input("Enter a number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")