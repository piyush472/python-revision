# Question 26: Reverse key value
# Write a Python program to swap keys and values in a dictionary.
d = {1: "piyush", 2: "rohan"}
di = {}
for key, values in d.items():
    di[values] = key
print(di)