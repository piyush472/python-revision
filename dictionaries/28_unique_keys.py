# Question 28: Unique keys
# Write a Python program to find keys present in one dict but not the other.
d1 = {1:"rohan", 2:"rohit", 3:"piyush"}
d2 = {1:"rohan", 22:"rohit", 3:"piyush"}
s=d1.keys() - d2.keys()
print(s)