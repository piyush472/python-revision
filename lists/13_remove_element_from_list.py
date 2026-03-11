# Question 13: Remove element from list
# Write a Python program to remove a specific element from a list and print the updated list.
l=[1,2,1,23,5,3,2,3,55,3,21,2,3,4]
given_ele=2
new_l=[]
for i in l:
    if i!=given_ele:
        new_l.append(i)
print(new_l)