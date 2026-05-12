# Question 33: Flatten nested dict
# Write a Python program to flatten a nested dictionary into a single-level dict.
d = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': {'f': 4, 'g': 5}}
d1 = {}
for key, value in d.items():
    if type(value) == dict:
        for k, v in value.items():
            d1[k] = v
    else:
        d1[key] = value
print(d1)
