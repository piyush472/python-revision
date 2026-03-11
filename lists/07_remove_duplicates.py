# Question 7: Remove duplicates
# Write a Python program to remove duplicate elements from a list and print the result.
l=[1,2,1,23,5,3,2,3,55,3,21,2,3,4]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)
