# Question 30: Filter by value
# Write a Python program to filter dictionary to keep only items where value > N.
d = {"a": 10, "b": 50, "c": 5, "d": 30, "e": 8}
N = 15
d2={}
for key,values in d.items():
    if values>N:
        d2[key]=values
print(d2)