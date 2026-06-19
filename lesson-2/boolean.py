### Boolean Data Type Questions:
# 1.Write a program that accepts a username and password and checks if both are not empty.
username = input("Enter username: ")
password = input("Enter password: ")
is_valid_login = len(username) > 0 and len(password) > 0
print(is_valid_login)


# # 2.Create a program that checks if two numbers are equal and outputs a message if they are.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
are_equal = (num1 == num2)
print(are_equal)


# 3.Write a program that checks if a number is positive and even.
num = int(input("Enter a number: "))
is_positive_and_even = (num > 0) and (num % 2 == 0)
print(is_positive_and_even)

# # 4. Write a program that takes three numbers and checks if all of them are different.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
all_different = (a != b) and (b != c) and (a != c)
print(all_different)

# #5. Create a program that accepts two strings and checks if they have the same length.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
same_length = (len(str1) == len(str2))
print(same_length)


# #6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.
num = int(input("Enter a number: "))
is_divisible_by_3_and_5 = (num % 3 == 0) and (num % 5 == 0)
print(is_divisible_by_3_and_5)

#7. Write a program that checks if the sum of two numbers is greater than 50
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
is_greater_than_50 = (num1 + num2) > 50
print(is_greater_than_50)

#8. Create a program that checks if a given number is between 10 and 20 (inclusive)
num = float(input("Enter a number: "))
is_in_range = 10 <= num <= 20
print(is_in_range)

