# Question 11: Find second largest element
# Write a Python program to find and print the second largest element in a list.
l=[1,2,1,23,5,3,2,3,55,3,21,2,3,4]
l2=[]
l.sort()
for i in l:
    if i not in l2:
        l2.append(i)
print("second largest ele in list",l2[1])