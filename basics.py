space = "----------------------------- \n"

# basic list comprehension:
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

print(f"Our numbers list is {new_list}. ")
print(f"Our new_list is {new_list}.")

print(space)
# ---------------------#

# basic list comprehension using .upper() modification and string
word = "airplane"
letters_list = [letter.upper() for letter in word]
print(f"Our word is {word}. ")
print(f"Our letters_list is {letters_list}.")

print(space)
# ---------------------#

# basic list comprehension using range and math operations
range_list = [i * 2 for i in range(1,5)]
print(f"Our range_list is {range_list}.")
print(space)
# ---------------------#

# basic list comprehension with conditional
names_list = ["John", "Sara", "Lucinda", "Kyle", "Bethany", "Derrick"]
short_names = [name for name in names_list if len(name) <= 4]

print(f"Our names_list is {names_list}. ")
print(f"Our short_names list is {short_names}.")
print(space)


# ---------------------#

# basic list comprehension with conditional and modification

mod_long_names = [name.upper() for name in names_list if len(name) > 5]
print(f"Our names_list is {names_list}. ")
print(f"Our mod_names list is {mod_long_names}.")
print(space)