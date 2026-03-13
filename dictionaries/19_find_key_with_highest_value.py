# Question 19: Find key with highest value
# Write a Python program to find the key with the highest value in a dictionary.

d = {
    "apple": 10,
    "banana": 20,
    "mango": 30,
    "orange": 15,
    "grapes": 25
}

maximum=max(d.values())
for key, value in d.items():
    if value==maximum:
        print(key)