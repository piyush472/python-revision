# Question 35: Top N values
# Write a Python program to find the top N keys with the highest values.
d = {"a": 10, "b": 50, "c": 30, "d": 80, "e": 20}
N = 3
l = []

sorted_keys = sorted(d, key=lambda k: d[k], reverse=True)  # returns LIST not dict
print(sorted_keys[:N])