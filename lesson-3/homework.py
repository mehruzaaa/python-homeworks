# HOMEWORK

### List Tasks
# 1. **Count Occurrences**: Given a list and an element, find how many times the element appears in the list.
numbers = [1, 2, 3, 4, 2, 2, 2]
element = 2
print(numbers.count(element))


# 2. **Sum of Elements**: Given a list of numbers, calculate the total of all the elements.
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))


# 3. **Max Element**: From a given list, determine the largest element.
numbers = [2, 3, 4, 6, 2]
print(max(numbers))


# 4. **Min Element**: From a given list, determine the smallest element.
numbers = [2, 3, 4, 6, 2]
print(min(numbers))


# 5. **Check Element**: Given a list and an element, check if the element is present in the list.
fruits = [ 'banana', 'apple', 'strawberry']
element = 'apple'
print(element in fruits)

# 6. **First Element**: Access the first element of a list, considering what to return if the list is empty.
# Scenario A: The list has items
fruits = ["apple", "banana", "cherry"]
if len(fruits) > 0:
    first_item = fruits[0]
else:
    first_item = "List is empty"
print(first_item)  

# Scenario B: The list is empty
empty_list = []
if len(empty_list) > 0:
    first_item = empty_list[0]
else:
    first_item = "List is empty"
print(first_item)  


#7. **Last Element**: Access the last element of a list, considering what to return if the list is empty.
fruits = ["apple", "banana", "cherry"]
if len(fruits) > 0:
    last_item = fruits[-1]
else:
    last_item = "List is empty"
print(last_item)  

# Scenario B: The list is empty
empty_list = []
if len(empty_list) > 0:
    last_item = empty_list[-1]
else:
    last_item = "List is empty"
print(last_item)


# 8. **Slice List**: Create a new list that contains only the first three elements of the original list.
list_org = [1, 2, 4, 6, 8]
print(list_org[:3])


# 9. **Reverse List**: Create a new list that contains the elements of the original list in reverse order.
list_org = [1, 2, 4, 6, 8]
print(list_org[::-1])

# 10. **Sort List**: Create a new list that contains the elements of the original list in sorted order.
list_org = [20, 30, 50, 30, 40, 6]
print(list_org)
print(sorted(list_org))


# 11. **Remove Duplicates**: Given a list, create a new list that contains only unique elements from the original list.
numbers = [1, 1, 2, 2, 4, 5, 7, 20]
print(set(numbers))


# 12. **Insert Element**: Given a list and an element, insert the element at a specified index.
fruits = ['apple', 'cherry', 'banana']
fruits.insert(1, 'watermelon')
print(fruits)


# 13. **Index of Element**: Given a list and an element, find the index of the first occurrence of the element.
fruits = ['apple', 'banana', 'cherry', 'banana']
element = 'banana'
print(fruits.index('banana'))


# 14. **Check for Empty List**: Determine if a list is empty and return a boolean.
list1 = [1]
print(bool(list1))

# 15. **Count Even Numbers**: Given a list of integers, count how many of them are even.
numbers = [1, 2, 3, 4, 5, 6, 7, 9]
even_count = len([num for num in numbers if num % 2 == 0])
print(even_count)


# 16. **Count Odd Numbers**: Given a list of integers, count how many of them are odd.
numbers = [1, 2, 3, 4, 5, 6, 7, 9]
odd_count = len([num for num in numbers if num % 2 != 0])
print(odd_count)


# 17. **Concatenate Lists**: Given two lists, create a new list that combines both lists.
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
print(list1 + list2)


# 18. **Find Sublist**: Given a list and a sublist, check if the sublist exists within the list.
main_list = [ 1, 2, 3, 4, 5, 6]
sublist = [3, 4]
print( str(sublist)[1:-1] in str(main_list))


# 19. **Replace Element**: Given a list, replace the first occurrence of a specified element with another element.
fruits = ['apple', 'banana', 'cherry', 'banana']
old_value = 'banana'
new_value = 'orange'
replace = fruits.index(old_value)
fruits[replace] = new_value
print(fruits)

# 22. **Filter Even Numbers**: Given a list of integers, create a new list that contains only the even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)


# 23. **Filter Odd Numbers**: Given a list of integers, create a new list that contains only the odd numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)


# 24. **List Length**: Determine the number of elements in the list.
# Original list of integers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(numbers))


# 25. **Create a Copy**: Create a new list that is a copy of the original list.
original_list = [1, 2, 3, 4, 5]
copied_list = original_list.copy()
print("Original:", original_list) 
print("Copied:", copied_list)    


# 31. **Repeat Elements**: Given a list and a number, create a new list where each element is repeated that number of times.
original_list = ['a', 'b', 'c']
multiplier = 3
result = original_list * multiplier
print(result)


# 32. **Merge and Sort**: Given two lists, create a new sorted list that merges both lists.
list_a = [3, 5, 1]
list_b = [4, 2, 6]
merged_sorted_list = sorted(list_a + list_b)
print(merged_sorted_list)


# 34. **Rotate List**: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])


# 35. **Create Range List**: Create a list of numbers in a specified range (e.g., from 1 to 10).
numbers = list(range(5, 10))
print(numbers)

# 36. **Sum of Positive Numbers**: Given a list of numbers, calculate the sum of all positive numbers.
numbers = [4, -3, 2, 0, -1, 7, -10]
positive_sum = sum(num for num in numbers if num > 0)
print(positive_sum)


# 37. **Sum of Negative Numbers**: Given a list of numbers, calculate the sum of all negative numbers.
numbers = [4, -3, 2, 0, -1, 7, -10]
negative_sum = sum(num for num in numbers if num < 0)
print(negative_sum)



 ### Tuple Tasks
# 1.**Count Occurrences**: Given a tuple and an element, find how many times 
fruits = ('apple', 'banana', 'apple', 'orange', 'apple', 'grape')
apple_count = fruits.count('apple')
print(apple_count)


# 2. **Max Element**: From a given tuple, determine the largest element.
numbers = (14, 52, 8, 91, 37, 25)
largest_element = max(numbers)
print(largest_element)


# 3. **Min Element**: From a given tuple, determine the smallest element.
numbers = (14, 52, 8, 91, 37, 25)
smallest_element = min(numbers)
print(smallest_element)


# 4. **Check Element**: Given a tuple and an element, check if the element is present in the tuple.
numbers = (1, 2, 3, 4, 5)
element = 2
print( element in numbers)


# 7. **Tuple Length**: Determine the number of elements in the tuple.
nuumbers = (1, 2, 3, 4, 5, 6)
print(len(numbers))


# 8. **Slice Tuple**: Create a new tuple that contains only the first three elements of the original tuple.
original_tuple = ('a', 'b', 'c', 'd', 'e')
first_three = original_tuple[0:3]
first_three_shorthand = original_tuple[:3]
print(first_three_shorthand)


# 9. **Concatenate Tuples**: Given two tuples, create a new tuple that combines both.
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
combined_tuple = tuple_a + tuple_b
print(combined_tuple)


# 10. **Check if Tuple is Empty**: Determine if a tuple has any elements.
numbers = (1, 2, 3)
print(numbers != 0)


# 14. **Create a Single Element Tuple**: Create a tuple that contains a single specified element.
single_element_tuple = (5,)
print(single_element_tuple)
print(type(single_element_tuple))


# 15. **Convert List to Tuple**: Given a list, create a tuple containing the same elements.
programming_languages = ["Python", "JavaScript", "Go"]
languages_tuple = tuple(programming_languages)
print(languages_tuple)
print(type(languages_tuple))


# 21. **Repeat Elements**: Given a tuple and a number, create a new tuple where each element is repeated that number of times.
original_tuple = ('a', 'b', 'c')
multiplier = 3
result = original_tuple * multiplier
print(result)


# 22. **Create Range Tuple**: Create a tuple of numbers in a specified range (e.g., from 1 to 10).
print(tuple(range(5, 10)))


# 23. **Reverse Tuple**: Create a new tuple that contains the elements of the original tuple in reverse order.
original = (1, 2, 3, 4, 5)
print(original[::-1])



### Set Tasks
# 1. **Union of Sets**: Given two sets, create a new set that contains all unique elements from both sets.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a | set_b  
print(result)  


# 2. **Intersection of Sets**: Given two sets, create a new set that contains elements common to both sets.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a & set_b  
print(result)  


# 3. **Difference of Sets**: Given two sets, create a new set with elements from the first set that are not in the second.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a - set_b  
print(result)  


# 4. **Check Subset**: Given two sets, check if one set is a subset of the other.
small_set = {1, 2}
big_set = {1, 2, 3, 4}
print(small_set.issubset(big_set)) 


# 5. **Check Element**: Given a set and an element, check if the element exists in the set.
my_set = {"apple", "banana", "cherry"}
print("apple" in my_set)  


# 6. **Set Length**: Determine the number of unique elements in a set.
my_set = {10, 20, 30, 40}
print(len(my_set))  


# 7. **Convert List to Set**: Given a list, create a new set that contains only the unique elements from that list.
my_list = [1, 2, 2, 3, 3, 3]
my_set = set(my_list)
print(my_set)  


# 8. **Remove Element**: Given a set and an element, remove the element if it exists.
my_set = {1, 2, 3}
my_set.discard(2)  
my_set.discard(99) 
print(my_set)  


# 9. **Clear Set**: Create a new empty set from an existing set.
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  


# 10. **Check if Set is Empty**: Determine if a set has any elements.
my_set = set()
if not my_set:
    print("The set is empty!")


# 11. **Symmetric Difference**: Given two sets, create a new set that contains elements that are in either set but not in both.
set_a = {1, 2, 3}
set_b = {3, 4, 5}
result = set_a ^ set_b  
print(result)  


# 12. **Add Element**: Given a set and an element, add the element to the set if it is not already present.
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  


# 13. **Pop Element**: Given a set, remove and return an arbitrary element from the set.
my_set = {10, 20, 30}
popped_item = my_set.pop()
print(popped_item)


# 14. **Find Maximum**: From a given set of numbers, find the maximum element.
numbers = {5, 2, 9, 1, 7}
print(max(numbers))  


# 15. **Find Minimum**: From a given set of numbers, find the minimum element.
numbers = {5, 2, 9, 1, 7}
print(min(numbers))  


# 16. **Filter Even Numbers**: Given a set of integers, create a new set that contains only the even numbers.
numbers = {1, 2, 3, 4, 5, 6}
evens = {n for n in numbers if n % 2 == 0}
print(evens)  


# 17. **Filter Odd Numbers**: Given a set of integers, create a new set that contains only the odd numbers.
numbers = {1, 2, 3, 4, 5, 6}
odds = {n for n in numbers if n % 2 != 0}
print(odds)  


# 18. **Create a Set of a Range**: Create a set of numbers in a specified range (e.g., from 1 to 10).
numbers_set = set(range(1, 11))
print(numbers_set)  


# 19. **Merge and Deduplicate**: Given two lists, create a new set that merges both lists and removes duplicates.
list_a = [1, 2, 3]
list_b = [3, 4, 5]
merged_set = set(list_a + list_b)
print(merged_set)  


# 20. **Check Disjoint Sets**: Given two sets, check if they have no elements in common.
set_a = {1, 2, 3}
set_b = {4, 5, 6}
print(set_a.isdisjoint(set_b))  

# 21. **Remove Duplicates from a List**: Given a list, create a set from it to remove duplicates, then convert back to a list.
original_list = [1, 2, 2, 3, 1, 4]
clean_list = list(set(original_list))
print(clean_list)  


# 22. **Count Unique Elements**: Given a list, determine the count of unique elements using a set.
my_list = ['apple', 'banana', 'apple', 'orange', 'banana']
unique_count = len(set(my_list))
print(unique_count)  



### Dictionary Tasks
# 1. **Get Value**: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.
inventory = {"apples": 10, "bananas": 5}
search_key = "pears"
if search_key in inventory:
    result = inventory[search_key]
else:
    result = 0  
print(result)


# 2. **Check Key**: Given a dictionary and a key, check if the key is present in the dictionary.
my_dict = {"name": "Alice", "age": 25}
print("name" in my_dict)  


# 3. **Count Keys**: Determine the number of keys in the dictionary.
my_dict = {"x": 10, "y": 20, "z": 30}
print(len(my_dict))  


# 4. **Get All Keys**: Create a list that contains all the keys in the dictionary
my_dict = {"apple": 1, "banana": 2}
keys_list = list(my_dict)
print(keys_list)  

# 5. **Get All Values**: Create a list that contains all the values in the dictionary.
my_dict = {"apple": 1, "banana": 2}
values_list = list(my_dict.values())
print(values_list)  


# 6. **Merge Dictionaries**: Given two dictionaries, create a new dictionary that combines both.
dict_a = {"x": 1, "y": 2}
dict_b = {"y": 20, "z": 3}
merged = dict_a | dict_b
print(merged)   


# 7. **Remove Key**: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.
my_dict = {"a": 1, "b": 2}
my_dict.pop("a", None)   
my_dict.pop("z", None)   
print(my_dict)  


# 8. **Clear Dictionary**: Create a new empty dictionary.
my_dict = {"status": "active"}
my_dict.clear()
print(my_dict)  


# 9. **Check if Dictionary is Empty**: Determine if a dictionary has any elements.
my_dict = {}
if not my_dict:
    print("Dictionary is empty!")


# 10. **Get Key-Value Pair**: Given a dictionary and a key, retrieve the key-value pair if the key exists.
my_dict = {"id": 101}
pair = ("id", my_dict["id"]) if "id" in my_dict else None
print(pair)  


# 11. **Update Value**: Given a dictionary, update the value for a specified key.
my_dict = {"score": 10}
my_dict["score"] = 15
print(my_dict) 


# 12. **Count Value Occurrences**: Given a dictionary, count how many times a specific value appears across the keys.
my_dict = {"alice": "admin", "bob": "user", "charlie": "admin"}
admin_count = list(my_dict.values()).count("admin")
print(admin_count)  


# 13. **Invert Dictionary**: Given a dictionary, create a new dictionary that swaps keys and values.
my_dict = {"a": 1, "b": 2}
inverted = {value: key for key, value in my_dict.items()}
print(inverted)  


# 14. **Find Keys with Value**: Given a dictionary and a value, create a list of all keys that have that value.
my_dict = {"low": 10, "mid": 50, "high": 50}
matched_keys = [k for k, v in my_dict.items() if v == 50]
print(matched_keys) 


# 15. **Create a Dictionary from Lists**: Given two lists (one of keys and one of values), create a dictionary that pairs them.
keys = ["name", "role"]
values = ["Alice", "Dev"]
new_dict = dict(zip(keys, values))
print(new_dict)  


# 16. **Check for Nested Dictionaries**: Given a dictionary, check if any values are also dictionaries.
data = {"user": "bob", "meta": {"age": 30}}
has_nested = any(isinstance(v, dict) for v in data.values())
print(has_nested)


# 17. **Get Nested Value**: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.
nested = {"outer": {"inner": "target_value"}}
print(nested["outer"]["inner"]) 


# 18. **Create Default Dictionary**: Create a dictionary that provides a default value for missing keys.
from collections import defaultdict
scores = defaultdict(int)
scores["points"] += 10 
print(dict(scores))  


# 19. **Count Unique Values**: Given a dictionary, determine the number of unique values it contains.
my_dict = {"a": 5, "b": 5, "c": 10}
unique_count = len(set(my_dict.values()))
print(unique_count)  


# 20. **Sort Dictionary by Key**: Create a new dictionary sorted by keys.
my_dict = {"c": 3, "a": 1, "b": 2}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict) 


# 23. **Check for Common Keys**: Given two dictionaries, check if they have any keys in common.
dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}
have_common = not set(dict_1).isdisjoint(set(dict_2))
print(have_common)  


# 24. **Create Dictionary from Tuple**: Given a tuple of key-value pairs, create a dictionary from it.
tuple_pairs = (("id", 42), ("status", "OK"))
generated_dict = dict(tuple_pairs)
print(generated_dict)  


# 25. **Get the First Key-Value Pair**: Retrieve the first key-value pair from a dictionary.
my_dict = {"first": 1, "second": 2, "third": 3}
first_pair = next(iter(my_dict.items()))
print(first_pair)  
