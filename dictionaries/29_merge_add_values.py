# Question 29: Merge add values
# Write a Python program to merge two dicts - if key exists in both, add the values.
d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"a": 5,  "b": 15, "d": 40}
d3 = {}

for i in d1.keys():
    if i not in d2:
        d3[i] = d1[i]
    else:
        d3[i] = d1[i] + d2[i]


for i in d2.keys():
    if i not in d1:
        d3[i] = d2[i]

print(d3)