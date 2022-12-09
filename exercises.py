#  Write a List Comprehension to create a new list called squared_numbers.
#  This new list should contain every number in the list numbers but each number should be squared.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# ------------------------------- #

# Write a List Comprehension to create a new list called result.
# This new list should only contain the even numbers from the list numbers.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)

# ------------------------------- #

# Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
# Create a list called result which contains the numbers that are common in both files.


with open("file1.txt") as file1:
    f1_data = file1.readlines()

with open("file2.txt") as file2:
    f2_data = file2.readlines()


result = [int(num) for num in f1_data if num in f2_data]
print(result)