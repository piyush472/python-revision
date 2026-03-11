# Question 12: Count occurrences of element
# Write a Python program to count how many times a given element appears in a list.
l=[1,2,1,23,5,3,2,3,55,3,21,2,3,4]
count=0
given_ele=2
for i in l:
    if i==given_ele:
        count+=1
print("count of given ele in list :",count)