# Question 17: Find difference between lists
# Write a Python program to find elements that are in one list but not in the other.
l=[]
l1=[1,2,3,4,5,2,35,32,23,32]
l2=[6,7,8,9,10,232,342,23,1,4354,223,4]
for i in l1:
    if i not in l2 and i not in l:
        l.append(i)
print(l)