# Question 16: Find common elements in lists
# Write a Python program to find and print the common elements between two lists.
l=[]
l1=[1,2,3,4,5,2,35,32,23,32]
l2=[6,7,8,9,10,232,342,23,1,4354,223,4]
for i in l2:
    if i in l1 and i not in l:
        l.append(i)
print(l)