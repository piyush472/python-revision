# Question 23: Remove empty elements
# Write a Python program to remove empty strings / None / falsy values from a list.
falsy_values = [False, None, 0, 0.0, "", '', [], (), {}, set()]
l1=[]
l = [1, "", None, 5, 0, "hello", False, [], {}, 7]
for i in l:
    if i not in falsy_values:
        l1.append(i)
print(l1)