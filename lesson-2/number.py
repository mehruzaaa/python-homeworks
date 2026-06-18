### Number Data Type Questions:
# 1.Create a program that takes a float number as input and rounds it to 2 decimal places.
num = float(input("Enter a decimal number:"))
rounded_num = round(num, 2)
print("Rounded number:", rounded_num)


# 2.Write a Python file that asks for three numbers and outputs the largest and smallest.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))
largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)
print("Largest number:", largest)
print("Smallest number:", smallest)


# 3.Create a program that converts kilometers to meters and centimeters.
km = int(input("Enter kilometer:"))
meters = km * 1000
centimeters = km * 100000
print(f"meters: {meters}, centimeters: {centimeters}")


# 4.Write a program that takes two numbers and prints out the result of integer division and the remainder.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

print(int(num1/ num2))
print(num1 % num2)


# 5.Make a program that converts a given Celsius temperature to Fahrenheit.
celsius = float(input("Enter temperature in Celsius:"))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius}℃ is equal to {fahrenheit}℉")


# 6.Create a program that accepts a number and returns the last digit of that number.
num = int(input("Enter a number:"))
last_digit = num % 10
print(last_digit)


# 7.Create a program that takes a number and checks if it’s even or not.
num = int(input("Enter a number:"))
print(num % 2)



