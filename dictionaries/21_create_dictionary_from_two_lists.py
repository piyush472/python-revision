# Question 21: Create dictionary from two lists
# Write a Python program to create a dictionary from two lists (one for keys, one for values).
keys = ["name", "age", "city", "course", "college"]

values = ["Piyush", 21, "Delhi", "BCA", "IGNOU"]
d={}
for i in range(len(keys)):
    key=keys[i]
    value=values[i]
    d[key]=value
print(d)