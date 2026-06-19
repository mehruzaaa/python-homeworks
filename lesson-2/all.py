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



### String Data Type Questions:
# 1.Create a program to ask name and year of birth from user and tell them their age.
name = input("Enter your name:")
year_of_birth = int(input("Enter your birth year:"))
age = 2026 - year_of_birth
print(f"Hi, {name}, your age is {age}")


# 3.Write a Python program to:
#- Take a string input from the user.
#- Print the length of the string.
#- Convert the string to uppercase and lowercase.
string = input("Enter a string:")
print(len(string))
print(string.upper())
print(string.lower())


# 4.Write a Python program to check if a given string is `palindrome` or not.
#> What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.
text = input("Enter a string:").lower()
reversed_text = text[::-1]
if text == reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


# 6.Write a Python program to check if one string contains another.
string1 = input("Enter string1:")
string2 = input("Enter string2:")
if string1 in string2 or string2 in string1:
    print("Yes, one string contains another")
else:
    print("No one string does not contain another")


# # 7.Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
sentence = input("Enter a sentence:")
to_replace = input("replace word:")
replace_with = input("with:")
print(sentence.replace(to_replace, replace_with))


# # 8.Write a program that asks the user for a string and prints the first and last characters of the string. 
string = input("Enter something:")
print(string[0:1])
print(string[-1:])


# 9.Ask the user for a string and print the reversed version of it.
string = input("Write something:")
print(string[::-1])


# 10.Write a program that asks the user for a sentence and prints the number of words in it.
sentence = input("Enter something:")
words = sentence.split()
print(len(words))


# 12.Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., `-` or `,`).  
words = ["I", "am", "learning", "Python"]
character = input("Enter a character:")
print(character.join(words))


# #13. Ask the user for a string and remove all spaces from it.  
string = input("Enter something:")
no_space = string.replace(" ", "")
print(no_space)


# #14.Write a program to ask for two strings and check if they are equal or not.  
str1 = input("Enter something:")
str2 = input("Enter something:")

if str1 == str2:
    print("Equal")
else:
    print("Not equal")


# 15.Ask the user for a sentence and create an acronym from the first letters of each word. 
phrase = input("Enter a phrase:")
words = phrase.split()
acronym = ""
for word in words:
    acronym = acronym + word[0]
print(acronym.upper())


# 16.Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  
string = input("Enter a string:")
char_to_remove = input("character to remove:")
print(string.replace(char_to_remove, ""))


# # 17.Ask the user for a string and replace all the vowels with a symbol (e.g., `*`). 
text = input("Enter a string: ")
symbol = "*"
vowels = "aeiouAEIOU"
result = ""
for char in text:
    if char in vowels:
        result += symbol
    else:
        result += char
print("Result:", result)


# 18.Write a program that checks if a string starts with one word and ends with another.
sentence = input("Enter a string:")
start = input("starts with:")
end = input("ends with:")
if sentence.startswith(start) and sentence.endswith(end):
    print("yes")
else:
    print("no")



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
