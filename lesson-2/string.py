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

