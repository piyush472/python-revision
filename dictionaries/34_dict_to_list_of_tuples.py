# Question 34: Dict to list of tuples
# Write a Python program to convert a dictionary to a list of (key, value) tuples.
d = {"a": 1, "b": 2, "c": 3}
l=[]
for key,value in d.items():
    l.append((key,value))
print(l)