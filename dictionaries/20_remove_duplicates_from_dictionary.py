# Question 20: Remove duplicates from dictionary
# Write a Python program to remove duplicate values from a dictionary (keep first occurrence).



d = {
    "apple": 10,
    "banana": 20,
    "mango": 20,
    "orange": 15,
    "grapes": 25
}

new_d = {}

for key, value in d.items():
    if value not in new_d.values():
        new_d[key] = value

print(new_d)