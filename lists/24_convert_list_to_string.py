# Question 24: Convert list to string
# Write a Python program to convert a list of items (strings or mixed) into a single string.
l = ["Age", 21, "City", "Delhi"]
s=""
for i in l:
    s.join(i)
print(s)