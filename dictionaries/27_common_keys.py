# Question 27: Common keys
# Write a Python program to find common keys between two dictionaries.
d1 = {1:"rohan", 2:"rohit", 3:"piyush"}
d2 = {1:"rohan", 22:"rohit", 3:"piyush"}

common = d1.keys() & d2.keys() 
print("common keys in both dict:", common)