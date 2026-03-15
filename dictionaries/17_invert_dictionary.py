# Question 17: Invert dictionary
# Write a Python program to invert a dictionary (swap keys and values - assume values are unique).
d = {
    "apple": 10,
    "banana": 20,
    "mango": 30,
    "orange": 40,
    "grapes": 50
}

new_d = {}

for key, value in d.items():
    new_d[value] = key

print(new_d)