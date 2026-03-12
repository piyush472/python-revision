# Question 15: Convert list to dictionary
# Write a Python program to convert two lists (keys and values) into a dictionary.
keys = ["name", "age", "city", "course", "college"]

values = ["Piyush", 21, "Delhi", "BCA", "IGNOU"]
d={}
for i in range(len(keys)):
    key=keys[i]
    value=values[i]
    d[key]=value
print(d)